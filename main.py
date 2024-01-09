import requests, json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

def City_temp(city: str):
  URL = BASE_URL + "q=" + city + "&units=metric" + "&appid=" + API_KEY
  print(URL)

  response = requests.get(URL)
  print("status code:", response.status_code) # Status code is 200. Add an if so that the code checks that is the status code before retrieving the data

  # Retrieving the data in json format
  data = response.json()
  # print(data)
  # https://openweathermap.org/weather-data 

  main = data['main']
  temp = main['temp']
  min_temp = main['temp_min']
  max_temp = main['temp_max']
  print('Min temp is:', int(min_temp)) # Min temp is: 14
  print('Max temp is:', int(max_temp)) # Max temp is: 19
  print('Current temp is:', int(temp)) # Current temp is: 17


  # Weather data is an array of 1 element that holds this:
  # 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]
  weather_array = data['weather']
  weather = weather_array[0]
  main_clouds = weather['main']
  print('There is:', main_clouds) # There is: Clouds


  sys = data['sys']
  sunset_utc = sys['sunset']
  sunrise_utc = sys['sunrise']
  sunset = datetime.fromtimestamp(sunset_utc)
  sunrise = datetime.fromtimestamp(sunrise_utc)
  print(f"Sunset is: {sunset:%H:%M}") # Sunset is: 16:59
  print(f"Sunrise is: {sunrise:%H:%M}") # Sunrise is: 06:56
  # TODO: convert from military time to standard time
  # TODO: Create seperate functions to return each of the data like printed above
  return int(temp)
