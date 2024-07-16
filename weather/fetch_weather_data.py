import time
import schedule
from django.core.management.base import BaseCommand
from weather.service import fetch_weather_data


class Command(BaseCommand):
    help = 'Store it in the database every 5 minutes'

    # Handles the fetched WeatherData and store DB every 5 minutes
    def handle(self, *args, **kwargs):
        def job():
            fetch_weather_data()

        schedule.every(5).minutes.do(job)

        while True:
            schedule.run_pending()
            time.sleep(1)
