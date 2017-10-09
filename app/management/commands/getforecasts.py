from __future__ import unicode_literals
from django.core.management.base import BaseCommand
from django.conf import settings

from app import tasks


class Command(BaseCommand):
    help = ('Fetch weather forecasts from a weather_url specified in the settings.APP and save them in the local \
            database.'
    )

    def handle(self, *args, **kwargs):
        url = settings.APP['weather_url']
        headers = settings.APP['headers']
        default_city = settings.APP['default_city']
        tasks.save_data(url, headers, default_city)
