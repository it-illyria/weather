from rest_framework import serializers

from .models import WeatherData


# ModelSerializer with the model fields
class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = [
            'current_temp', 'feels_like', 'weather_description', 'timestamp'
        ]
