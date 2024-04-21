import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
from main import city_temp

load_dotenv()

SPOTIFY_CLIENT_ID=os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET=os.getenv("SPOTIFY_CLIENT_SECRET")

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET))


def get_tempo(playlist_id: str) -> dict:
  track_tempo = {}

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
  return track_tempo
      

def get_track_id(playlist_id):
    track_id = {}

    # Get Playlist using its ID
    playlist = spotify.playlist_items(playlist_id)
    tracks = playlist['items']

    # Ensure I get all the tracks
    while playlist['next']:
      playlist = spotify.next(playlist)
      tracks.extend(playlist['items'])

    for track in tracks:
      track_id[track['track']['name']] = track['track']['id']
    return track_id


def calculate_recommendation(playlist: dict, city: str):
  temperature = city_temp(city)
  
  for track in playlist.copy():
    if temperature < 20 and playlist[track] < 120:
      return f"{track}, {playlist[track]}, {temperature}"
      
    elif temperature > 20 and playlist[track] > 120:
      return f"{track}, {playlist[track]}, {temperature}"