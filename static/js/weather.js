function refreshWeatherData() {
    fetch('')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                displayError(data.error);
            } else {
                updateWeatherDisplay(data);
            }
        })

}

function displayError(errorMessage) {
    const weatherList = document.querySelector('.weather-list');
    weatherList.innerHTML = `<p class="error-message">${errorMessage}</p>`;
}

function updateWeatherDisplay(data) {
    const weatherList = document.querySelector('.weather-list');

    // Clear existing weather data
    weatherList.innerHTML = '';

    if (data.length === 0) {
        weatherList.innerHTML = '<p>No weather data available.</p>';
        return;
    }

    // Most recent update
    const recentUpdate = createWeatherItem(data[0], true);
    weatherList.appendChild(recentUpdate);

    // Historic updates
    data.slice(1).forEach(weatherData => {
        const historicItem = createWeatherItem(weatherData, false);
        weatherList.appendChild(historicItem);
    });
}

function createWeatherItem(weatherData, isRecent) {
    const weatherItem = document.createElement('div');
    weatherItem.classList.add('weather-item');
    if (isRecent) {
        weatherItem.classList.add('recent-update');
    }

    // Update HTML content for each weather item
    weatherItem.innerHTML = `
        <div class="location-info">
            <p>${new Date(weatherData.timestamp_full).toLocaleString()}</p>
            <p>Tirana, Albania</p>
        </div>
        <div class="main-weather-info">
            <img src="{% static 'images/' %}${weatherData.icon}" alt="weather icon">
            <h2>${weatherData.current_temp} °C</h2>
            <h4 class="feels-like">Feels Like: ${weatherData.feels_like}°</h4>
            <h4 class="description">${weatherData.weather_description}</h4>
        </div>
    `;

    return weatherItem;
}

// Initial data fetch
refreshWeatherData();

// Refresh every 5 minutes
setInterval(refreshWeatherData, 5 * 60 * 1000);
