from django.db import models
from django.contrib.auth.models import User


class Crop(models.Model):
    CROP_CHOICES = [
        ('wheat', 'Wheat'),
        ('rice', 'Rice'),
        ('corn', 'Corn'),
        ('cotton', 'Cotton'),
        ('sugarcane', 'Sugarcane'),
        ('soybean', 'Soybean'),
        ('tomato', 'Tomato'),
        ('potato', 'Potato'),
        ('onion', 'Onion'),
        ('groundnut', 'Groundnut'),
    ]
    name = models.CharField(max_length=100, choices=CROP_CHOICES)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
    market_name = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    trend = models.CharField(max_length=10, choices=[('up', 'Rising'), ('down', 'Falling'), ('stable', 'Stable')], default='stable')

    def __str__(self):
        return f"{self.get_name_display()} - {self.market_name}"


class FarmerListing(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    crop = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    asking_price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crop} by {self.farmer.username}"
