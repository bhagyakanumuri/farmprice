import requests
from django.core.cache import cache
from django.conf import settings

CROP_API_NAMES = {
    'wheat': 'Wheat',
    'rice': 'Rice',
    'tomato': 'Tomato',
    'onion': 'Onion',
    'potato': 'Potato',
    'corn': 'Maize',
    'cotton': 'Cotton',
    'soybean': 'Soyabean',
    'groundnut': 'Groundnut',
    'sugarcane': 'Sugarcane',
    'chilli': 'Dry Chillies',
    'turmeric': 'Turmeric',
    'jowar': 'Jowar',
    'bajra': 'Bajra',
    'sunflower': 'Sunflower Seed',
    'mango': 'Mango',
    'banana': 'Banana',
    'blackgram': 'Black Gram (Urd Beans)(Whole)',
    'greengram': 'Green Gram (Whole)',
}

AP_TELANGANA_STATES = ['Andhra Pradesh', 'Telangana']


def fetch_mandi_prices(commodity='Wheat', limit=10, state=None):
    cache_key = f"mandi_{commodity.lower()}_{state or 'all'}"
    cached = cache.get(cache_key)
    if cached:
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
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        records = data.get("records", [])
        cache.set(cache_key, records, 60 * 60)
        return records
    except Exception as e:
        print(f"API error for {commodity}: {e}")
        return []


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


def get_all_prices(state=None):
    results = []
    for crop_key in CROP_API_NAMES.keys():
        summary = get_price_summary(crop_key, state=state)
        if summary:
            results.append(summary)
    return results


def get_ap_telangana_prices():
    results = []
    for state in AP_TELANGANA_STATES:
        for crop_key in CROP_API_NAMES.keys():
            summary = get_price_summary(crop_key, state=state)
            if summary:
                results.append(summary)
    return results