import requests
from geopy.geocoders import Nominatim

from .models import WeatherData


def fetch_weather_data():
    api_url = 'https://melchior.moja.it:8085/weather-api/get_weather'
    params = {
        'lat': '41.3281007',
        'lon': '139.6917'
    }
    response = requests.get(api_url, params=params)
    data = response.json()

    # Create a new instance of WeatherData with fetched data
    WeatherData.objects.create(
        current_temp=data['current_temp'],
        feels_like=data['feels_like'],
        weather_description=data['weather_description']
    )


def get_location_name(lat, lon):
    # Initialize Nominatim geocoder
    geolocator = Nominatim(user_agent="geoquiz_app")

    # Construct location query
    location = geolocator.reverse((lat, lon))

    # Extract location name
    return location.address
