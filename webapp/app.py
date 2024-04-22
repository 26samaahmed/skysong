# Flask
from flask import Flask, render_template, request
from markupsafe import escape
from main import city_temp, min_temp, max_temp, sunset_time, sunrise_time
from calculations import calculate_recommendation

app = Flask(__name__)

@app.route('/')
def display():
  # If requesting info about a specific city
  if request.method == "GET":
    # If the user has yet to submit the name of a specific city/ is visiting the page for the first time, then display the start page asking for the city
    if request.args.get("city") == None: # Extract the city name from the URL
      return render_template("index.html")
    
    # If user attempts to click submit button without entering a city name to request the temp for
    elif request.args.get("city") == '':
        return "Invalid, Please enter a city"
    
    # If the user submits a city then display the temperature by calling the function from main.py and pass the input as the function's arguments.
    else:
      city_name = request.args.get("city")
      playlist_id = "https://open.spotify.com/playlist/37i9dQZF1E36mCM83KV1pv"
      temperature = city_temp(city_name)
      minimum_temp = min_temp(city_name)
      maximum_temp = max_temp(city_name)
      sunset = sunset_time(city_name)
      sunrise = sunrise_time(city_name)
      song_id = calculate_recommendation(playlist_id, city_name)
      return render_template("response.html", city=city_name, temperature=temperature, minimum_temperature=minimum_temp, maximum_temperature=maximum_temp, sunset=sunset, sunrise=sunrise, song_id=song_id) 
    