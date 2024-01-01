#TODO: start by retrieving the current weather for 1 city
  #future implementation: have a page at the beginning that asks for what city the person wants to see the weather for
import requests
import os
from dotenv import load_dotenv

load_dotenv()
base_url = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.getenv("API_KEY")
