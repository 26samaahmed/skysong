import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID=os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET=os.getenv("SPOTIFY_CLIENT_SECRET")

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET))


def get_tempo(playlist_id: str) -> dict:
  tracks_dict = {}
  tempo = {}

  # Get Playlist using its ID
  playlist = spotify.playlist_items(playlist_id)
  tracks = playlist['items']

  # Ensure I get all the tracks
  while playlist['next']:
    playlist = spotify.next(playlist)
    tracks.extend(playlist['items'])

  # Get each track's name [made it into a dict where song name is the key and the uri is the value]
  for track in tracks:
    tracks_dict[track['track']['name']] = track['track']['uri']
    #print(track['track']['name'], ":", track['track']['uri'])

  return tracks_dict
  

playlist_id1 = 'spotify:playlist:37i9dQZF1E37LFLUC2Op3u'
playlist_id2 = 'spotify:playlist:37i9dQZF1E36mu0j5Hw95G'
playlist_id3 = 'spotify:playlist:37i9dQZF1E36mCM83KV1pv'
r1 = get_tempo(playlist_id1)
r2 = get_tempo(playlist_id2)
r3 = get_tempo(playlist_id3)
print(r1)
print(r2)
print(r3)

#TODO: Get the tempo for each song now that I have the names.

'''
ari = pd.DataFrame({'name':song_name,
                    'tempo':tempo
})
ari.head()
  '''