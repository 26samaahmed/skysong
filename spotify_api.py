import os
from dotenv import load_dotenv
import base64
from requests import post
import json

load_dotenv()

SPOTIFY_CLIENT_ID=os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET=os.getenv("SPOTIFY_CLIENT_SECRET")

def get_access_token():
    authorization_string = SPOTIFY_CLIENT_ID + ":" + SPOTIFY_CLIENT_SECRET

    # Convert the authorization string to bytes usinf UTF-8 encoding
    authorization_bytes = authorization_string.encode("utf-8")

    # Convert the bytes into a base64 encoded string
    authorization_base64 = str(base64.b64encode(authorization_bytes), "utf-8")

    # NOTE: Base 64 is a binary to text encoding scheme which converts binary data to ASCII characters

    # The URL to which the POST requests will be made
    url = "https://accounts.spotify.com/api/token"
    headers = {
        # authenticate using my client id and secret
        "Authorization" : 'Basic ' + authorization_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    # Specify that I'm using the client credentials authorization
    data = {"grant_type" : "client_credentials"}

    # Make a post request to the url with the headers and data i specified
    result = post(url, headers=headers, data=data)

    # Parse the json content to get the access token
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_aut_headers(token):
    return {"Authorization": "Bearer " + token}