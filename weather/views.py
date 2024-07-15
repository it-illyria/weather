from django.shortcuts import render
from .models import WeatherData
from .service import fetch_weather_data


def weather_view(request):
    fetch_weather_data()

    weather_data = WeatherData.objects.order_by('-timestamp')[:12].values()
    context = {
        'weather_data': weather_data
    }
    return render(request, 'html/weather.html', context)
