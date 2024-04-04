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
    #print(track['track']['name'], ":", spotify.audio_features(track['track']['uri'])[0]['tempo'])
    track_tempo[track['track']['name']] = spotify.audio_features(track['track']['uri'])[0]['tempo']
  return track_tempo

#TODO: Do the algorthm that will compare the current temperature to a song with a similar tempo

# Break down to smaller parts: get each individual calculcation and find the correlation
# Fast tempo: 120bpm < x
# Medium tempo: 120 bpm > x
# High temperature: 20ºC > x
# Low temeprature: 20ºC < x
def calculate_recommendation(playlist_id, city):

  # Loop through the list of songs tempo which is the dict's values
  # Return the first match I find.
  # Logic Problem with that is sometimes i would be recommending the same song and not moving on to the next as the hour changes
  temperature = city_temp(city)
  
  for track in playlist_id:
    if temperature < 20 and playlist_id[track] < 120:
      return f"{track}, {playlist_id[track]}, {temperature}"
    elif temperature > 20 and playlist_id[track] > 120:
      return f"{track}, {playlist_id[track]}, {temperature}"
      
  
id1 = 'spotify:playlist:6178cj0ubqnzFU3q3ovsnm'
r = get_tempo(id1)

# playlist_id1 = 'spotify:playlist:37i9dQZF1E37LFLUC2Op3u'
# playlist_id2 = 'spotify:playlist:37i9dQZF1E36mu0j5Hw95G'
# playlist_id3 = 'spotify:playlist:37i9dQZF1E36mCM83KV1pv'

result = calculate_recommendation(r, "Irvine")
print(result)