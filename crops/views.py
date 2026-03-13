from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Crop, FarmerListing
from .api_client import get_all_prices, get_price_summary, fetch_mandi_prices, CROP_API_NAMES
import json
from datetime import date, timedelta


def home(request):
    home_crops = ['wheat', 'rice', 'tomato', 'onion']
    live_prices = []
    for crop in home_crops:
        summary = get_price_summary(crop)
        if summary:
            live_prices.append(summary)

    recommendations = []
    for crop in live_prices:
        if crop['trend'] == 'up':
            action, reason, color = "SELL NOW", "Prices are rising", "green"
        elif crop['trend'] == 'down':
            action, reason, color = "HOLD", "Prices falling, wait", "red"
        else:
            action, reason, color = "MONITOR", "Prices are stable", "yellow"

        recommendations.append({
            "crop": crop['display_name'],
            "action": action,
            "reason": reason,
            "price": str(int(crop['current_price'])),
            "color": color,
        })

    listings = FarmerListing.objects.filter(is_available=True)[:4]
    context = {
        'crops': live_prices,
        'listings': listings,
        'recommendations': recommendations,
    }
    return render(request, 'crops/home.html', context)


def crop_prices(request):
    state_filter = request.GET.get('state', '')
    crop_filter = request.GET.get('crop', '').lower()
    region = request.GET.get('region', '')

    if state_filter:
        all_prices = get_all_prices(state=state_filter)
    else:
        all_prices = get_all_prices()

    if crop_filter:
        all_prices = [c for c in all_prices if crop_filter in c['name']]

    states = ['Andhra Pradesh', 'Telangana', 'Tamil Nadu', 'Karnataka',
              'Maharashtra', 'Punjab', 'Uttar Pradesh', 'Rajasthan']

    context = {
        'crops': all_prices,
        'states': states,
        'state_filter': state_filter,
        'crop_filter': crop_filter,
        'region': region,
    }
    return render(request, 'crops/prices.html', context)


def price_prediction(request):
    crop_name = request.GET.get('crop', 'wheat')
    today = date.today()

    commodity = CROP_API_NAMES.get(crop_name, crop_name.capitalize())
    records = fetch_mandi_prices(commodity, limit=30)

    labels = []
    historical = []
    predicted = []

    if records:
        real_prices = []
        for r in reversed(records):
            try:
                price = float(r.get("modal_price", 0))
                arrival_date = r.get("arrival_date", "")
                if price > 0:
                    real_prices.append((arrival_date, price))
            except:
                pass

        for i, (d, p) in enumerate(real_prices[-30:]):
            labels.append(d)
            historical.append(p)

        while len(historical) < 30:
            labels.insert(0, "")
            historical.insert(0, historical[0] if historical else 2000)

        if len(historical) >= 7:
            recent = historical[-7:]
            weights = [1, 1, 2, 2, 3, 3, 4]
            weighted_avg = sum(w * p for w, p in zip(weights, recent)) / sum(weights)
            trend = (historical[-1] - historical[-7]) / 7
        else:
            weighted_avg = historical[-1] if historical else 2000
            trend = 0

        last_price = weighted_avg
        for i in range(1, 16):
            d = today + timedelta(days=i)
            labels.append(d.strftime("%b %d"))
            historical.append(None)
            last_price = last_price + (trend * 0.85) + (last_price * 0.002)
            predicted.append(round(last_price, 2))

    else:
        base_price = {"wheat": 2200, "rice": 1900, "corn": 1500, "tomato": 700, "onion": 1000}.get(crop_name, 2000)
        for i in range(30, 0, -1):
            d = today - timedelta(days=i)
            labels.append(d.strftime("%b %d"))
            historical.append(base_price + (i * 2))

        last_price = historical[-1]
        for i in range(1, 16):
            d = today + timedelta(days=i)
            labels.append(d.strftime("%b %d"))
            historical.append(None)
            last_price = int(last_price * 1.01)
            predicted.append(last_price)

    current_price = historical[29] if len(historical) > 29 and historical[29] else 2000
    max_pred = max(predicted) if predicted else current_price
    best_day_idx = predicted.index(max_pred) if predicted else 0
    best_sell_date = today + timedelta(days=best_day_idx + 1)
    profit_percent = round((max_pred - current_price) / current_price * 100, 1) if current_price else 0

    if profit_percent > 5:
        action = "SELL LATER"
        advice = f"Prices expected to rise {profit_percent}%. Wait for best price."
    elif profit_percent < -3:
        action = "SELL NOW"
        advice = "Prices expected to fall. Sell as soon as possible."
    else:
        action = "MONITOR"
        advice = "Prices stable. Monitor daily before deciding."

    recommendation = {
        "action": action,
        "advice": advice,
        "best_date": best_sell_date.strftime("%B %d, %Y"),
        "expected_price": round(max_pred, 2),
        "current_price": round(current_price, 2),
        "profit_percent": profit_percent,
    }

    crop_choices = ['wheat', 'rice', 'corn', 'tomato', 'onion', 'cotton', 'soybean', 'potato']
    context = {
        'crop_name': crop_name,
        'labels': json.dumps(labels),
        'historical': json.dumps([h for h in historical if h is not None]),
        'predicted': json.dumps(predicted),
        'recommendation': recommendation,
        'crop_choices': crop_choices,
    }
    return render(request, 'crops/prediction.html', context)


def weather_advice(request):
    location = request.GET.get('location', 'Punjab')
    weather = {
        'location': location,
        'temp': 28,
        'humidity': 65,
        'condition': 'Partly Cloudy',
        'rainfall_chance': 30,
        'wind': '12 km/h',
        'forecast': [
            {'day': 'Today', 'icon': '⛅', 'temp': 28, 'rain': '30%'},
            {'day': 'Tomorrow', 'icon': '🌧️', 'temp': 24, 'rain': '80%'},
            {'day': 'Day 3', 'icon': '🌧️', 'temp': 22, 'rain': '70%'},
            {'day': 'Day 4', 'icon': '🌤️', 'temp': 26, 'rain': '20%'},
            {'day': 'Day 5', 'icon': '☀️', 'temp': 30, 'rain': '10%'},
        ],
        'advice': [
            {'crop': 'Wheat', 'advice': 'Harvest before rainfall tomorrow. Sell within 2 days.', 'urgency': 'high'},
            {'crop': 'Rice', 'advice': 'Good moisture for growth. Hold for 1 week.', 'urgency': 'low'},
            {'crop': 'Vegetables', 'advice': 'Transport to market before rain. Prices may drop.', 'urgency': 'medium'},
            {'crop': 'Cotton', 'advice': 'Protect from heavy rain. Delay harvest by 3 days.', 'urgency': 'medium'},
        ]
    }
    return render(request, 'crops/weather.html', {'weather': weather, 'location': location})


@login_required
def sell_crop(request):
    if request.method == 'POST':
        FarmerListing.objects.create(
            farmer=request.user,
            crop=request.POST['crop'],
            quantity=request.POST['quantity'],
            asking_price=request.POST['asking_price'],
            location=request.POST['location'],
            phone=request.POST.get('phone', ''),
            description=request.POST.get('description', ''),
        )
        messages.success(request, 'Your listing has been posted!')
        return redirect('marketplace')
    crop_choices = ['Wheat', 'Rice', 'Corn', 'Cotton', 'Sugarcane', 'Soybean',
                    'Tomato', 'Potato', 'Onion', 'Groundnut', 'Chilli', 'Turmeric',
                    'Blackgram', 'Greengram']
    return render(request, 'crops/sell.html', {'crop_choices': crop_choices})


def marketplace(request):
    listings = FarmerListing.objects.filter(is_available=True).order_by('-created_at')
    crop_filter = request.GET.get('crop', '')
    location_filter = request.GET.get('location', '')
    if crop_filter:
        listings = listings.filter(crop__icontains=crop_filter)
    if location_filter:
        listings = listings.filter(location__icontains=location_filter)
    return render(request, 'crops/marketplace.html', {
        'listings': listings,
        'crop_filter': crop_filter,
        'location_filter': location_filter,
    })


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return render(request, 'crops/register.html')
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, f'Welcome to FarmPrice, {username}!')
        return redirect('home')
    return render(request, 'crops/register.html')


def user_login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('home')
        messages.error(request, 'Invalid credentials.')
    return render(request, 'crops/login.html')


def user_logout(request):
    logout(request)
    return redirect('home')
from django.utils import translation

def set_language_view(request, lang_code):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code, max_age=365*24*60*60)
    translation.activate(lang_code)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang_code
    return response