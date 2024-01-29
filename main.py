import requests
from bs4 import BeautifulSoup

# date = input("Informe a data da lista que deseja, no seguinte formato YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/2024-01-06")
billboard_page = response.text

soup = BeautifulSoup(billboard_page, "html.parser")

song_titles = soup.find_all(name="h3", class_="u-max-width-230@tablet-only")
song_list = []

for song in song_titles:
    song_name = " ".join(song.text.split())
    song_list.append(song_name)

print(song_list)
