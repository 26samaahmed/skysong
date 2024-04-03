import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID=os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET=os.getenv("SPOTIFY_CLIENT_SECRET")

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET))


def get_track_name(playlist_id: str) -> list:
  track_names = []

  # Get Playlist using its ID
  playlist = spotify.playlist_items(playlist_id)
  tracks = playlist['items']

  # Ensure I get all the tracks
  while playlist['next']:
    playlist = spotify.next(playlist)
    tracks.extend(playlist['items'])

  # Get each track's name
  for track in tracks:
    track_names.append(track['track']['name'])

  return track_names

playlist_id1 = 'spotify:playlist:37i9dQZF1E37LFLUC2Op3u'
playlist_id2 = 'spotify:playlist:37i9dQZF1E36mu0j5Hw95G'
playlist_id3 = 'spotify:playlist:37i9dQZF1E36mCM83KV1pv'
r1 = get_track_name(playlist_id1)
r2 = get_track_name(playlist_id2)
r3 = get_track_name(playlist_id3)
print(r1)
print(r2)
print(r3)

#TODO: Get the tempo for each song now that I have the names. Reference code below

'''
song_name = []
song_uri = []
album = []
count = 0
for j in uri:
    
    tracks = sp.album_tracks(j)   
    for i in tracks['items']:
        album.append(name[count])
        song_name.append(i['name'])
        song_uri.append(i['uri'])
    count+=1
song_name
acoustic = []
dance = []
energy = []
instrumental = []
liveness = []
loudness = []
speech = []
tempo = []
valence = []
popularity = []

for i in song_uri:
    feat = sp.audio_features(i)[0]
    acoustic.append(feat['acousticness'])
    dance.append(feat['danceability'])
    energy.append(feat['energy'])
    speech.append(feat['speechiness'])
    instrumental.append(feat['instrumentalness'])
    loudness.append(feat['loudness'])
    tempo.append(feat['tempo'])
    liveness.append(feat['liveness'])
    valence.append(feat['valence'])
    popu = sp.track(i)
    popularity.append(popu['popularity'])
    ari = pd.DataFrame({'name':song_name,
                    'album':album,
                    'dance':dance,
                    'acoustic':acoustic,
                    'energy':energy,
                    'instrumental':instrumental,
                    'liveness':liveness,
                    'loudness':loudness,
                    'speech':speech,
                    'tempo':tempo,
                    'valence':valence,
                    'popularity':popularity
    
})
ari.head()
  '''