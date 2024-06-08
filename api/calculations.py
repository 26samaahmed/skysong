import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import datetime
from dotenv import load_dotenv
from api.main import city_temp

load_dotenv()

SPOTIFY_CLIENT_ID=os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET=os.getenv("SPOTIFY_CLIENT_SECRET")

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET))

recommendation_history = {}
today = datetime.datetime.now().strftime("%Y-%m-%d")

def calculate_recommendation(playlist_id: str, city: str):
  global recommendation_history, today
  track_tempo = {}
  track_id = {}

  # Get Playlist using its ID
  playlist = spotify.playlist_items(playlist_id)
  tracks = playlist['items']

  # Ensure I get all the tracks
  while playlist['next']:
    playlist = spotify.next(playlist)
    tracks.extend(playlist['items'])

  for track in tracks:
    # Retrieve the tempo for each song using its URI
    track_tempo[track['track']['name']] = spotify.audio_features(track['track']['uri'])[0]['tempo']
    track_id[track['track']['name']] = track['track']['id']

  temperature = city_temp(city)
  
  # Check if it's a new day and reset the recommendation history
  current_date = datetime.datetime.now().strftime("%Y-%m-%d")
  if current_date != today:
    recommendation_history = {}
    today = current_date

  for track in track_tempo:
    if temperature < 20 and track_tempo[track] < 120:
      # Make sure that songs are not recommended more than once a day
      if track not in recommendation_history:
        recommendation_history[track] = today
        return track_id[track]
      
    elif temperature > 20 and track_tempo[track] > 120:
      if track not in recommendation_history:
        recommendation_history[track] = today
        return track_id[track]
