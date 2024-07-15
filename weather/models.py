from django.db import models


class WeatherData(models.Model):
    current_temp = models.FloatField()
    feels_like = models.FloatField()
    weather_description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.weather_description} at {self.current_temp}°C"
