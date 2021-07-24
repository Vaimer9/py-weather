import requests
import json

class Weather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def getWeather(self, city_name):
        
        complete_url = f'{self.base_url}appid={self.api_key}&q={city_name}'
        response = requests.get(complete_url)
        data = response.json()
        if data["cod"] != "404":
 
            y = data["main"]

            current_temperature = y["temp"]

            current_pressure = y["pressure"]

            current_humidity = y["humidity"]

            z = data["weather"]
        
            weather_description = z[0]["description"]

            return [current_temperature, current_pressure, current_humidity, weather_description]

        else:
            return "Invalid City name"
