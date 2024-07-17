function refreshWeatherData() {
    fetch('/weather/').then(response => response.json()).then(data => {
            updateWeatherDisplay(data);
    }).catch(error => {
            console.error('Error fetching weather data:', error);
    });
}

function updateWeatherDisplay(data) {
    const weatherList = document.querySelector('.weather-list');
    if (data.length === 0) {
        return;
    }

    // Updates the most recently weather data
    const recentUpdate = weatherList.querySelector('.weather-item.recent-update');
    updateWeatherItem(recentUpdate, data[0]);

    // Updates the historic of the Weather data from before
    const remainingItems = weatherList.querySelectorAll('.weather-item:not(.recent-update)');
    remainingItems.forEach((item, index) => {
        updateWeatherItem(item, data[index + 1]);
    });
}

function updateWeatherItem(weatherItemElement, weatherData) {
  weatherItemElement.querySelector('.weather-location span').textContent = `${new Date(weatherData.timestamp).toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric', hour: 'numeric', minute: 'numeric' })}`;
  weatherItemElement.querySelector('.weather-current-temp strong').textContent = `${weatherData.current_temp}°C`;
}

refreshWeatherData();

// Refresh every 5 minutes (adjust as needed)
setInterval(refreshWeatherData, 5 * 60 * 1000);
