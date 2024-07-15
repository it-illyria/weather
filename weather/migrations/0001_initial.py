# Generated by Django 5.0.7 on 2024-07-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_last_updated', models.DateTimeField(auto_now=True, verbose_name='Data last updated')),
                ('current_temp', models.FloatField()),
                ('feels_like', models.FloatField()),
                ('weather_description', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
