from django.shortcuts import render
from django.utils import timezone

from .models import WeatherData
from .serializers import WeatherDataSerializer
from .service import fetch_weather_data

# weather description to SVG
WEATHER_ICON_MAPPING = {
    'clear sky': '1.svg',
    'broken clouds': '3.svg',
    'overcast clouds': '6.svg',
    'scattered clouds': '4.svg',
    'few clouds': '2.svg',
}


# Retrieve and display weather_data
def weather_view(request):
    last_data = WeatherData.objects.latest('timestamp')
    if not last_data or (timezone.now() - last_data.timestamp).total_seconds() > 5 * 60:
        fetch_weather_data()

    weather_data = WeatherData.objects.order_by('-timestamp')[:13].values()
    serializer = WeatherDataSerializer(weather_data, many=True)

    for data in serializer.data:
        data['icon'] = WEATHER_ICON_MAPPING.get(data['weather_description'], 'default.svg')
    sliced_weather_data = serializer.data[1:]

    context = {
        'weather_data': sliced_weather_data,
    }

    return render(request, 'html/weather.html', context)
