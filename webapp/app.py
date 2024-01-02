# Flask
from flask import Flask, render_template
from main import city_temp

app = Flask(__name__)

@app.route("/")
def display():
  result = city_temp()
  return render_template('index.html' , result=result)