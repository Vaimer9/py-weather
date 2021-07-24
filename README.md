# py-weather
This is a simple weather API wrapper made in python which uses [Openweather](https://openweathermap.org/) to get weather info for any place on the globe.

# Quick Start
First to get started you need to get yourself an API key from [Openweather](https://openweathermap.org/). Log in and confirm your email to get access to use the API key.
Once that is complete you can make an instance of the weather class in your code
```
my_data = Weather(api_key="your_api_key_here")
```
And then call the `getWeather` method to get the weather information.
```
my_data.getWeather(city_name="name_of_the_city")
```
Once done you can print out the values of my_data to see how the values are structured and how you want to return them.

# FAQ
1. What values does the `getWeather()` method return  
ans. It returns in the following manner `[current_temperature, current_pressure, current_humidity, weather_description]`
 