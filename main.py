#TODO: start by retrieving the current weather for 1 city
  #future implementation: have a page at the beginning that asks for what city the person wants to see the weather for
import requests, json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

city = "Irvine"
URL = BASE_URL + "q=" + city + "&units=metric" + "&appid=" + API_KEY
print(URL)

response = requests.get(URL)
print(response.status_code) # Status code is 200. Add an if so that the code checks that is the status code before retrieving the data

# Retrieving the data in json format
data = response.json()
# print(data)
'''
   {'coord': {'lon': -117.8231, 'lat': 33.6695}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 
   'base': 'stations', 'main': {'temp': 291.72, 'feels_like': 291.02, 'temp_min': 289.72, 'temp_max': 294.16, 'pressure': 1017, 'humidity': 53}, 
   'visibility': 10000, 'wind': {'speed': 3.6, 'deg': 230}, 'clouds': {'all': 20}, 'dt': 1704153284, 'sys': {'type': 1, 'id': 5876, 'country': 'US', 'sunrise': 1704120948, 'sunset': 1704156797}, 
   'timezone': -28800, 'id': 5359777, 'name': 'Irvine', 'cod': 200}
'''

# https://openweathermap.org/weather-data 

main = data['main']
temp = main['temp']
print("Temperature: ",temp) # Prints-> Temperature:  18.27 (celsius)