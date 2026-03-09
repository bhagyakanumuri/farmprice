import requests
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


def fetch_and_save_prices(state=None):
    url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
    params = {
        "api-key": settings.DATA_GOV_API_KEY,
        "format": "json",
        "limit": 100,
    }
    if state:
        params["filters[state.keyword]"] = state

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        return data.get("records", [])
    except Exception as e:
        print(f"API error: {e}")
        return []


def fetch_mandi_prices(commodity='Wheat', limit=30, state=None):
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
        return data.get("records", [])
    except Exception as e:
        print(f"API error for {commodity}: {e}")
        return []


def get_all_prices(state=None):
    from .models import Crop
    crops = Crop.objects.all()
    if state:
        crops = crops.filter(state__iexact=state)
    results = []
    for c in crops:
        results.append({
            "name": c.name,
            "display_name": c.get_name_display(),
            "current_price": float(c.current_price),
            "min_price": float(c.min_price),
            "max_price": float(c.max_price),
            "market_name": c.market_name,
            "state": c.state,
            "updated_at": str(c.updated_at.date()),
            "trend": c.trend,
        })
    return results


def get_price_summary(crop_key, state=None):
    from .models import Crop
    crops = Crop.objects.filter(name=crop_key)
    if state:
        crops = crops.filter(state__iexact=state)
    c = crops.first()
    if not c:
        return None
    return {
        "name": c.name,
        "display_name": c.get_name_display(),
        "current_price": float(c.current_price),
        "min_price": float(c.min_price),
        "max_price": float(c.max_price),
        "market_name": c.market_name,
        "state": c.state,
        "updated_at": str(c.updated_at.date()),
        "trend": c.trend,
    }