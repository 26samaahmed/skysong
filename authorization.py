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
    authorization_bytes = authorization_string.encode("utf-8")
    # Encode using Base 64
    authorization_base64 = str(base64.b64encode(authorization_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : 'Basic ' + authorization_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type" : "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

token = get_access_token()
print(token)