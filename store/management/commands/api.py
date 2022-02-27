from django.core.management.base import BaseCommand

import requests

url = f"https://www.zalando.fr/baskets-luxe-homme/"




response = requests.request("GET", url)

print(response.status_code)

class Command(BaseCommand):

    def handle(self, *args, **options):
        return response.status_code
