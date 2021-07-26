from weather import Weather

lot = Weather('8011f7d9cbadc12924e1dc1952335279')

york = lot.getWeather('Haridwar')

print(f'Temprature: {round(york["temprature"])}C\nPressure: {round(york["pressure"])} Pascal\nHumidity: {york["humidity"]} g.m-3\nWeather Condition: {york["description"]}')