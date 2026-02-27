from crops.models import Crop
Crop.objects.create(name="wheat", current_price=2340, min_price=2100, max_price=2500, market_name="Amritsar Mandi", state="Punjab", trend="up")
Crop.objects.create(name="rice", current_price=1980, min_price=1800, max_price=2200, market_name="Karnal Mandi", state="Haryana", trend="up")
Crop.objects.create(name="tomato", current_price=850, min_price=600, max_price=1200, market_name="Nashik Mandi", state="Maharashtra", trend="up")
Crop.objects.create(name="onion", current_price=1200, min_price=900, max_price=1500, market_name="Lasalgaon Mandi", state="Maharashtra", trend="up")
Crop.objects.create(name="potato", current_price=720, min_price=600, max_price=900, market_name="Agra Mandi", state="Uttar Pradesh", trend="stable")
print("Done! 5 crops added!")
exit()