import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# includes artist id
txt = 'spotify:artist:0ghlgldX5Dd6720Q3qFyQB'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(txt, album_type='album')
albums = results['items']
while results['next']:
  results = spotify.next(results)
  albums.extend(results['items'])

for album in albums:
  print(album['name'])
