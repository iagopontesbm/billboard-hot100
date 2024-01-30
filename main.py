import requests
import spotify as sp
from bs4 import BeautifulSoup

date = input("Informe a data da lista que deseja, no seguinte formato YYYY-MM-DD: ")

# 1 - Scraping the Billboard Hot 100
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
billboard_page = response.text

soup = BeautifulSoup(billboard_page, "html.parser")

song_titles = soup.find_all(name="h3", class_="u-max-width-230@tablet-only")
song_list = []

for song in song_titles:
    song_name = " ".join(song.text.split())
    song_list.append(song_name)

print(f"Lista de músicas: {song_list}")

# 3 - Search Spotify for the Songs from Step 1
music_uri_list = []
print("Pesquisando músicas!")
for song in song_list:
    song_name = sp.search_music(song)
    music_uri_list.append(song_name)

# 4 - Creating Spotify Playlist
print("Criando playlist.")
playlist_id = sp.create_playlist(f"Playlist Billboard {date}")

# 5 - Adding to Spotify Playlist
print("Adicionado músicas a playlist.")
sp.add_music_playlist(playlist_id, music_uri_list)
