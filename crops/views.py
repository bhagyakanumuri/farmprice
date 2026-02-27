from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Crop, FarmerListing
import json
import random
from datetime import date, timedelta


def home(request):
    crops = Crop.objects.all()[:6]
    listings = FarmerListing.objects.filter(is_available=True)[:4]
    recommendations = [
        {"crop": "Wheat", "action": "SELL NOW", "reason": "Prices at 3-month high", "price": "2340", "color": "green"},
        {"crop": "Rice", "action": "HOLD", "reason": "Monsoon expected to raise prices", "price": "1980", "color": "yellow"},
        {"crop": "Tomato", "action": "SELL SOON", "reason": "Supply increasing next week", "price": "850", "color": "orange"},
        {"crop": "Onion", "action": "SELL NOW", "reason": "Festival demand peak", "price": "1200", "color": "green"},
    ]
    context = {
        'crops': crops,
        'listings': listings,
        'recommendations': recommendations,
    }
    return render(request, 'crops/home.html', context)


def crop_prices(request):
    state_filter = request.GET.get('state', '')
    crop_filter = request.GET.get('crop', '')
    crops = Crop.objects.all()
    if state_filter:
        crops = crops.filter(state__icontains=state_filter)
    if crop_filter:
        crops = crops.filter(name__icontains=crop_filter)
    states = Crop.objects.values_list('state', flat=True).distinct()
    context = {'crops': crops, 'states': states, 'state_filter': state_filter, 'crop_filter': crop_filter}
    return render(request, 'crops/prices.html', context)


def price_prediction(request):
    crop_name = request.GET.get('crop', 'wheat')
    today = date.today()
    labels = []
    historical = []
    predicted = []
    base_price = {"wheat": 2200, "rice": 1900, "corn": 1500, "tomato": 700, "onion": 1000}.get(crop_name, 2000)
    for i in range(30, 0, -1):
        d = today - timedelta(days=i)
        labels.append(d.strftime("%b %d"))
        historical.append(base_price + random.randint(-200, 200))
    last_price = historical[-1]
    for i in range(1, 16):
        d = today + timedelta(days=i)
        labels.append(d.strftime("%b %d"))
        historical.append(None)
        last_price = int(last_price * random.uniform(0.98, 1.04))
        predicted.append(last_price)
    max_pred = max(predicted)
    best_day_idx = predicted.index(max_pred)
    best_sell_date = today + timedelta(days=best_day_idx + 1)
    recommendation = {
        "action": "SELL" if max_pred > historical[29] * 1.05 else "HOLD",
        "best_date": best_sell_date.strftime("%B %d, %Y"),
        "expected_price": max_pred,
        "current_price": historical[29],
        "profit_percent": round((max_pred - historical[29]) / historical[29] * 100, 1),
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
            description=request.POST.get('description', ''),
        )
        messages.success(request, 'Your listing has been posted!')
        return redirect('marketplace')
    crop_choices = ['Wheat', 'Rice', 'Corn', 'Cotton', 'Sugarcane', 'Soybean', 'Tomato', 'Potato', 'Onion', 'Groundnut']
    return render(request, 'crops/sell.html', {'crop_choices': crop_choices})


def marketplace(request):
    listings = FarmerListing.objects.filter(is_available=True)
    crop_filter = request.GET.get('crop', '')
    if crop_filter:
        listings = listings.filter(crop__icontains=crop_filter)
    return render(request, 'crops/marketplace.html', {'listings': listings, 'crop_filter': crop_filter})


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
