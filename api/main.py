import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

# Helper function that makes the requests to be called in any function where data needs to be retrieved
def base_url(city: str):
  URL = BASE_URL + "?q=" + city + "&appid=" + API_KEY + "&units=metric"
  response = requests.get(URL)
  data = response.json() # Retrieve the data in json format
  return data

def city_temp(city: str):
  data = base_url(city)
  main = data['main']
  temp = main['temp']
  return int(temp)

def max_temp(city: str):
  data = base_url(city)
  main = data['main']
  max_temp = main['temp_max']
  return int(max_temp)

def min_temp(city: str):
  data = base_url(city)
  main = data['main']
  min_temp = main['temp_min']
  return int(min_temp)

def sunset_time(city: str):
  data = base_url(city)
  sys = data['sys']
  sunset_utc = sys['sunset']
  sunset = datetime.fromtimestamp(sunset_utc)
  hour = sunset.hour
  if hour > 12:
    hour = hour - 12
  return f"Sunset is at {hour}:{sunset:%M} PM" # Using %M to get the minute from the datetime object which is sunset

def sunrise_time(city: str):
  data = base_url(city)
  sys = data['sys']
  sunrise_utc = sys['sunrise']
  sunrise = datetime.fromtimestamp(sunrise_utc)
  return f"Sunrise is at {sunrise:%H:%M} AM"
