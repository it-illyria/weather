from rest_framework import serializers
from .models import WeatherData


# ModelSerializer with the model fields
class WeatherDataSerializer(serializers.ModelSerializer):
    timestamp_full = serializers.DateTimeField(source='timestamp', format="%A %d/%m/%Y %H:%M")
    timestamp_short = serializers.DateTimeField(source='timestamp', format="%H:%M")

    class Meta:
        model = WeatherData
        fields = [
            'current_temp', 'feels_like', 'weather_description', 'timestamp_full', 'timestamp_short'
        ]
