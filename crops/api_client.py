import requests
from django.core.cache import cache
from django.conf import settings

CROP_API_NAMES = {
    'wheat': 'Wheat',
    'rice': 'Rice',
    'tomato': 'Tomato',
    'onion': 'Onion',
    'potato': 'Potato',
    'cotton': 'Cotton',
    'groundnut': 'Groundnut',
    'chilli': 'Dry Chillies',
    'turmeric': 'Turmeric',
    'blackgram': 'Black Gram (Urd Beans)(Whole)',
    'greengram': 'Green Gram (Whole)',
}


def fetch_all_mandi_prices(state=None):
    """Fetch all crops in ONE API call instead of many"""
    safe_state = state.replace(' ', '_') if state else 'all'
    cache_key = f"all_mandi_{safe_state}"

    cached = cache.get(cache_key)
    if cached is not None:
        return cached

    url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
    params = {
        "api-key": settings.DATA_GOV_API_KEY,
        "format": "json",
        "limit": 100,
    }

    if state:
        params["filters[state.keyword]"] = state

    try:
        response = requests.get(url, params=params, timeout=15)
        data = response.json()
        records = data.get("records", [])
        cache.set(cache_key, records, 60 * 60)
        return records
    except Exception as e:
        print(f"API error: {e}")
        cache.set(cache_key, [], 60 * 5)
        return []


def fetch_mandi_prices(commodity='Wheat', limit=30, state=None):
    """Fetch prices for a single commodity - used for predictions"""
    safe_key = commodity.lower().replace(' ', '_').replace('(', '').replace(')', '')
    safe_state = state.replace(' ', '_') if state else 'all'
    cache_key = f"mandi_{safe_key}_{safe_state}"

    cached = cache.get(cache_key)
    if cached is not None:
        return cached

    url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
    params = {
        "api-key": settings.DATA_GOV_API_KEY,
        "format": "json",
        "limit": limit,
        "filters[commodity]": commodity,
    }

    if state:
        params["filters[state.keyword]"] = state

    try:
        response = requests.get(url, params=params, timeout=15)
        data = response.json()
        records = data.get("records", [])
        cache.set(cache_key, records, 60 * 60)
        return records
    except Exception as e:
        print(f"API error for {commodity}: {e}")
        cache.set(cache_key, [], 60 * 5)
        return []


def process_records(records):
    """Convert raw API records into crop summaries"""
    crop_map = {}

    for r in records:
        commodity = r.get("commodity", "").strip()
        # Find matching crop key
        crop_key = None
        for key, name in CROP_API_NAMES.items():
            if name.lower() == commodity.lower():
                crop_key = key
                break
        if not crop_key:
            continue

        try:
            price = float(r.get("modal_price", 0))
            if price <= 0:
                continue
        except:
            continue

        if crop_key not in crop_map:
            crop_map[crop_key] = {
                "name": crop_key,
                "display_name": commodity,
                "prices": [],
                "market_name": r.get("market", "N/A"),
                "state": r.get("state", "N/A"),
                "updated_at": r.get("arrival_date", "N/A"),
            }
        crop_map[crop_key]["prices"].append(price)

    results = []
    for crop_key, data in crop_map.items():
        prices = data["prices"]
        if not prices:
            continue
        avg = round(sum(prices) / len(prices), 2)
        trend = 'stable'
        if len(prices) >= 2:
            if prices[0] > prices[-1] * 1.02:
                trend = 'up'
            elif prices[0] < prices[-1] * 0.98:
                trend = 'down'

        results.append({
            "name": crop_key,
            "display_name": data["display_name"],
            "current_price": avg,
            "min_price": min(prices),
            "max_price": max(prices),
            "market_name": data["market_name"],
            "state": data["state"],
            "updated_at": data["updated_at"],
            "trend": trend,
        })

    return results


def get_all_prices(state=None):
    records = fetch_all_mandi_prices(state=state)
    return process_records(records)


def get_price_summary(crop_key, state=None):
    commodity = CROP_API_NAMES.get(crop_key, crop_key.capitalize())
    records = fetch_mandi_prices(commodity, limit=10, state=state)

    if not records:
        return None

    prices = []
    for r in records:
        try:
            prices.append(float(r.get("modal_price", 0)))
        except:
            pass

    if not prices:
        return None

    avg = round(sum(prices) / len(prices), 2)
    latest = records[0]

    trend = 'stable'
    if len(prices) >= 2:
        if prices[0] > prices[-1] * 1.02:
            trend = 'up'
        elif prices[0] < prices[-1] * 0.98:
            trend = 'down'

    return {
        "name": crop_key,
        "display_name": commodity,
        "current_price": avg,
        "min_price": min(prices),
        "max_price": max(prices),
        "market_name": latest.get("market", "N/A"),
        "state": latest.get("state", "N/A"),
        "updated_at": latest.get("arrival_date", "N/A"),
        "trend": trend,
    }