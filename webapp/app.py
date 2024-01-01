# Flask
from flask import Flask
app = Flask(__name__)

@app.route("/city")
def display():
  return "<p> Hello World <\p>"