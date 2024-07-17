import requests
from django.http import JsonResponse

from .models import WeatherData


# Fetch WeatherData from the API with params
def fetch_weather_data():
    api_url = 'https://melchior.moja.it:8085/weather-api/get_weather'
    params = {
        'lat': '41.323250',
        'lon': '19.794187'
    }
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        WeatherData.objects.create(
            current_temp=data['current_temp'],
            feels_like=data['feels_like'],
            weather_description=data['weather_description']
        )
    except requests.RequestException as e:
        error_message = str(e)
        if 'Rate limit exceeded' in error_message:
            return JsonResponse({'error': 'Rate limit exceeded'}, status=429)
        else:
            return JsonResponse({'error': 'Failed to fetch weather data'}, status=500)
