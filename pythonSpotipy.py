import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="23376b3f6e3f41c4864b4d334ef8a552",
                                                                                client_secret="4007cce00fd7400a9211a0bf1ffd5d3e"))
"""
results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])"""

results = spotify.search(q="Mexico", limit=10)
for idx, track in enumerate(results["tracks"]["items"]):
    print(idx, track["name"])