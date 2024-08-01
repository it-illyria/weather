import logging
import requests
from django.http import JsonResponse

from weather_project import settings
from .models import WeatherData

logger = logging.getLogger(__name__)


def fetch_weather_data():
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = settings.OPENWEATHERMAP_API_KEY

    params = {
        'lat': '41.323250',
        'lon': '19.794187',
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Check for expected data structure
        if 'main' not in data or 'weather' not in data:
            raise ValueError('Invalid API response')

        # Extract data
        current_temp = data['main']['temp']
        feels_like = data['main'].get('feels_like', 'N/A')
        weather_description = data['weather'][0]['description']

        # Save to database
        weather_data = WeatherData.objects.create(
            current_temp=current_temp,
            feels_like=feels_like,
            weather_description=weather_description
        )

        return weather_data

    except requests.RequestException as e:
        logger.error(f"API request error: {e}")
        if '401' in str(e):
            return JsonResponse({'error': 'Invalid API key'}, status=401)
        elif '429' in str(e):
            return JsonResponse({'error': 'Rate limit exceeded'}, status=429)
        else:
            return JsonResponse({'error': 'Failed to fetch weather data'}, status=500)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return JsonResponse({'error': 'An unexpected error occurred'}, status=500)
