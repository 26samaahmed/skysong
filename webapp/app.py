# Flask
from flask import Flask, render_template, request
from main import City_temp

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
    
    # If the user submitted a city then display the temperature by calling the function from main.py and pass the input as the function's arguments. The temperature will be returned.
    else:
      city_name = request.args.get("city")
      temperature = City_temp(city_name)
      return render_template("response.html", city=city_name, temperature=temperature) # city and temperature are the value passed to HTML tempelate for rendering