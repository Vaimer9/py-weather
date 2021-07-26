import requests
import json

class Weather:
    def __init__(self, api_key, unit = "metric"):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
        self.unit = unit

    def getWeather(self, city_name):
        
        complete_url = f'{self.base_url}appid={self.api_key}&q={city_name}&units={self.unit}'
        response = requests.get(complete_url)
        data = response.json()
        if data["cod"] != "404":
 
            main_info = data["main"]
            description = data["weather"]
            wind_info = data["wind"]

            current_temperature = main_info["temp"]
            current_pressure = main_info["pressure"]
            current_humidity = main_info["humidity"]
            wind_speed = wind_info["speed"]
            wind_direction = wind_info["deg"]


            
        
            weather_description = description[0]["description"]

            info = {
                "temprature": current_temperature,
                "pressure": current_pressure,
                "humidity": current_humidity,
                "description": weather_description,
                "wind_speed": wind_speed,
                "wind_direction": wind_direction
            }

            return info

        else:
            return "Invalid City name"
