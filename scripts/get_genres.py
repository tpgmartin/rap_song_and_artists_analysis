from bs4 import BeautifulSoup
import csv
import pandas as pd
import re
import requests

base_url = "https://en.wikipedia.org/wiki/"

def get_genres_for_artist(artist):

    # special case
    if artist == "BrockHampton":
        artist = artist.upper()

    parsed_artist = "_".join(artist.split(" "))

    url = base_url + parsed_artist
    permutations = ["", "_(rapper)", "_(musician)", "_(band)"]

    for permutation in permutations:
        search_url = url + permutation
        response = requests.get(search_url)

        genres = []
        if response.status_code == 200:
            html = BeautifulSoup(response.text, "html5lib")
            infobox = html.find("table", class_="infobox")

            try:
                for tr in infobox.find_all('tr'):
                    if "Genres" in tr.text:
                        for a_tag in tr.find_all('a'):
                            genres.append(a_tag.contents[0])
            except:
                pass
        
        if len(genres) > 0:
            break
    
    genres = [genre for genre in genres if not any(char.isdigit() for char in genre)]
    return genres

if __name__ == "__main__":

    artists = pd.read_csv("./data/target_artists.csv")["artist"]

    artists_by_genres = []
    for artist in artists:
        genres_for_artist = get_genres_for_artist(artist)
        artists_by_genres.append((artist, genres_for_artist))

    with open("./data/artists_by_genres.csv", "w") as f:
        w = csv.writer(f)
        w.writerow(["artist", "genres"])
        for row in artists_by_genres:
            w.writerow([row[0], row[1]])
        