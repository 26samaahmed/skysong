import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import pandas as pd

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
    # Retrieve the tempo for each song using it's URI
    track_tempo[track['track']['name']] = spotify.audio_features(track['track']['uri'])[0]['tempo']
  return track_tempo
  

# playlist_id1 = 'spotify:playlist:37i9dQZF1E37LFLUC2Op3u'
# playlist_id2 = 'spotify:playlist:37i9dQZF1E36mu0j5Hw95G'
# playlist_id3 = 'spotify:playlist:37i9dQZF1E36mCM83KV1pv'