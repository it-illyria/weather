from django.shortcuts import render
from geopy.geocoders import Nominatim
from .models import WeatherData
from .service import fetch_weather_data, get_location_name

# Define weather description to SVG mapping
WEATHER_ICON_MAPPING = {
    'clear sky': '1.svg',
    'broken clouds': '3.svg',
    'overcast clouds': '6.svg',
    'scattered clouds': '4.svg',
}


def weather_view(request):
    fetch_weather_data()

    weather_data = WeatherData.objects.order_by('-timestamp')[:13].values()

    # Map icons to weather descriptions
    for data in weather_data:
        data['icon'] = WEATHER_ICON_MAPPING.get(data['weather_description'], 'default.svg')
        data['location_name'] = get_location_name(data.get('lat'), data.get('lon'))
    context = {
        'weather_data': weather_data
    }
    return render(request, 'html/weather.html', context)


def get_location_name(lat, lon):
    # Initialize Nominatim geocoder
    geolocator = Nominatim(user_agent="geoquiz_app")

    # Construct location query
    location = geolocator.reverse((lat, lon))

    # Extract location name
    return location.address
