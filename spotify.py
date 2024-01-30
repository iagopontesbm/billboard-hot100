import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# 2 - Authentication with Spotify
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

auth_manager = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://example.com", scope="playlist-modify-private")
sp = spotipy.Spotify(auth_manager=auth_manager)

# id usuário
current_user = sp.current_user()
user_id = current_user['id']


def search_music(music_name: str) -> str:
    """Retorna o URI da música pesquisada"""
    music_search = sp.search(q=music_name, limit=1, offset=0, type="track", market=None)
    music_uri = music_search["tracks"]["items"][0]['uri']
    return music_uri


def create_playlist(playlist_name: str) -> str:
    """"Criar playlist e retorna o id"""
    new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, collaborative=False, description="Playlist Billboard Natal")
    playlist_id = new_playlist["id"]
    return playlist_id


def add_music_playlist(playlist_id: str, music_uri_list: list) -> None:
    """Adiciona uma lista de URI/URL a playlist"""
    sp.playlist_add_items(playlist_id, music_uri_list)
