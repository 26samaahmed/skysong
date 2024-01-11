#TODO: start by retrieving the current weather for 1 city
  #future implementation: have a page at the beginning that asks for what city the person wants to see the weather for
import requests, json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

# Helper function that makes the requests to be called in any function where data needs to be retrieved
def base_url(city: str):
  URL = BASE_URL + "q=" + city + "&units=metric" + "&appid=" + API_KEY
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

# TODO: convert from military time to standard time
def sunset_time(city: str):
  data = base_url(city)
  sys = data['sys']
  sunset_utc = sys['sunset']
  sunset = datetime.fromtimestamp(sunset_utc)
  return f"Sunset is: {sunset:%H:%M}"

def sunrise_time(city: str):
  data = base_url(city)
  sys = data['sys']
  sunrise_utc = sys['sunrise']
  sunrise = datetime.fromtimestamp(sunrise_utc)
  return f"Sunrise is: {sunrise:%H:%M}"