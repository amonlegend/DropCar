# your_app/management/commands/load_locations.py

import json
from django.core.management.base import BaseCommand
from inventory.models import Location  # Import your Location model
import os

class Command(BaseCommand):
    help = 'Load locations data from JSON fixture'

    def handle(self, *args, **kwargs):
        try:
            # Path to your JSON fixture file
            json_file = os.path.join('inventory', 'fixtures', 'locations.json')

            # Open and load JSON data from the fixture file with the specified encoding
            with open(json_file, 'r', encoding='utf-8-sig') as f:
                data = json.load(f)

            # Iterate over the JSON data and create Location objects
            for item in data:
                location_name = item['location']
                Location.objects.create(location=location_name)

            self.stdout.write(self.style.SUCCESS('Locations data loaded successfully'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error loading locations data: {e}'))
