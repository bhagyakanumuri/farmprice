from django.core.management.base import BaseCommand
from crops.models import Crop
from crops.api_client import fetch_and_save_prices, CROP_API_NAMES

STATES = ['Andhra Pradesh', 'Telangana', 'Tamil Nadu', 'Karnataka',
          'Maharashtra', 'Punjab', 'Uttar Pradesh', 'Rajasthan']

class Command(BaseCommand):
    help = 'Fetch latest mandi prices and save to database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Fetching prices...')
        
        for state in STATES:
            self.stdout.write(f'Fetching {state}...')
            records = fetch_and_save_prices(state=state)
            
            for r in records:
                commodity = r.get("commodity", "").strip()
                crop_key = None
                for key, name in CROP_API_NAMES.items():
                    if name.lower() == commodity.lower():
                        crop_key = key
                        break
                if not crop_key:
                    continue

                try:
                    modal = float(r.get("modal_price", 0))
                    min_p = float(r.get("min_price", 0))
                    max_p = float(r.get("max_price", 0))
                    if modal <= 0:
                        continue

                    obj, created = Crop.objects.update_or_create(
                        name=crop_key,
                        state=r.get("state", state),
                        defaults={
                            "current_price": modal,
                            "min_price": min_p,
                            "max_price": max_p,
                            "market_name": r.get("market", ""),
                            "trend": "stable",
                        }
                    )
                    action = "Created" if created else "Updated"
                    self.stdout.write(f'{action}: {commodity} in {state}')
                except Exception as e:
                    self.stdout.write(f'Error: {e}')

        self.stdout.write(self.style.SUCCESS('Done! Prices updated.'))