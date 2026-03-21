from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('prices/', views.crop_prices, name='crop_prices'),
    path('predict/', views.price_prediction, name='price_prediction'),
    path('weather/', views.weather_advice, name='weather_advice'),
    path('sell/', views.sell_crop, name='sell_crop'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('lang/<str:lang_code>/', views.set_language_view, name='set_language'),
]