
from crops.models import Crop

sample_data = [
    {"name": "wheat", "current_price": 2340, "min_price": 2100, "max_price": 2500, "market_name": "Amritsar Mandi", "state": "Punjab", "trend": "up"},
    {"name": "wheat", "current_price": 2280, "min_price": 2050, "max_price": 2450, "market_name": "Ludhiana Mandi", "state": "Punjab", "trend": "stable"},
    {"name": "rice", "current_price": 1980, "min_price": 1800, "max_price": 2200, "market_name": "Karnal Mandi", "state": "Haryana", "trend": "up"},
    {"name": "rice", "current_price": 1920, "min_price": 1750, "max_price": 2100, "market_name": "Patna Mandi", "state": "Bihar", "trend": "stable"},
    {"name": "corn", "current_price": 1540, "min_price": 1400, "max_price": 1700, "market_name": "Davangere Mandi", "state": "Karnataka", "trend": "down"},
    {"name": "tomato", "current_price": 850, "min_price": 600, "max_price": 1200, "market_name": "Nashik Mandi", "state": "Maharashtra", "trend": "up"},
    {"name": "onion", "current_price": 1200, "min_price": 900, "max_price": 1500, "market_name": "Lasalgaon Mandi", "state": "Maharashtra", "trend": "up"},
    {"name": "potato", "current_price": 720, "min_price": 600, "max_price": 900, "market_name": "Agra Mandi", "state": "Uttar Pradesh", "trend": "stable"},
    {"name": "cotton", "current_price": 6800, "min_price": 6200, "max_price": 7200, "market_name": "Rajkot Mandi", "state": "Gujarat", "trend": "up"},
    {"name": "soybean", "current_price": 4200, "min_price": 3900, "max_price": 4500, "market_name": "Indore Mandi", "state": "Madhya Pradesh", "trend": "stable"},
    {"name": "groundnut", "current_price": 5100, "min_price": 4700, "max_price": 5500, "market_name": "Junagadh Mandi", "state": "Gujarat", "trend": "down"},
    {"name": "sugarcane", "current_price": 340, "min_price": 300, "max_price": 380, "market_name": "Muzaffarnagar Mandi", "state": "Uttar Pradesh", "trend": "stable"},
]

for data in sample_data:
    Crop.objects.create(**data)

print(f"✅ Created {len(sample_data)} crop price records!")
