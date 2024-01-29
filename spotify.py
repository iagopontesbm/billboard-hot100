import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

auth_manager = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://example.com", scope="playlist-modify-private")
sp = spotipy.Spotify(auth_manager=auth_manager)

current_user = sp.current_user()
user_id = current_user['id']
# print(user_id)

# id musica spotify
# music_search = sp.search(q="Rockin' Around The Christmas Tree", limit=1, offset=0, type="track", market=None)
# print(music_search["tracks"]["items"][0]["album"]["uri"])

# Criar playlist
#new_playlist = sp.user_playlist_create(user=user_id, name="Playlist de Natal", public=False, collaborative=False, description="Playlist Billboard Natal")
#playlist_id = new_playlist["id"]
#print(playlist_id)

sp.current_user_follow_playlist('52exwQf8X1EJniVH5Poffo')

playlists = sp.user_playlists(user_id)
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
