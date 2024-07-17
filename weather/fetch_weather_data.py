import logging
import time
import schedule
from django.core.management.base import BaseCommand
from weather.service import fetch_weather_data
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Store weather data in the database every 5 minutes'

    # Handles the fetched WeatherData and store DB every 5 minutes
    def handle(self, *args, **kwargs):
        def job():
            try:
                fetch_weather_data()
            except Exception as e:
                logger.error(f"Failed to fetch weather data: {e}")

        schedule.every(5).minutes.do(job)

        while True:
            schedule.run_pending()
            time.sleep(1)
