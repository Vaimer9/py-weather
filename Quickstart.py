# Import from the file
from weather import Weather

your_api_key = ''
city_name = ''

# Create an instance of weather object
instance = Weather(your_api_key)

# Make a dictionary filled with information about the city by this method
data = instance.getWeather(city_name)

# This is just an example of how you should be printing this
temprature = f'Temprature: {round(data["temprature"])}°C'
pressure = f'Pressure: {round(data["pressure"])} Pascal'
humidity = f'Humidity: {data["humidity"]} g.m-3'
weather_condition = f'Weather Condition: {data["description"]}'
wind_speed = f'Wind Speed: {data["wind_speed"]} m/s'
wind_direction = f'Wind Direction: {data["wind_direction"]}°'


print(f'{temprature} \n{pressure} \n{humidity} \n{weather_condition} \n{wind_speed} \n{wind_direction}')