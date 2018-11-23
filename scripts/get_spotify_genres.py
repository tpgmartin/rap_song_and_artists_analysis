import config
import csv
import requests
import pandas as pd

base_url = "https://api.spotify.com/v1/search"

def get_genres_for_artist(artist):

    querystring = {
        "q": artist,
        "type": "artist"
    }

    headers = { 'Authorization': "Bearer {}".format(config.SPOTIFY_CONFIG["BEARER_TOKEN"]) }

    response = requests.request("GET", base_url, headers=headers, params=querystring)

    return response.json()["artists"]["items"][0]["genres"]

if __name__ == "__main__":

    artists = pd.read_csv("./data/artists_with_at_least_20_tracks.csv")["artist"]

    artists_by_genres = []
    for artist in artists:
        genres_for_artist = get_genres_for_artist(artist)
        artists_by_genres.append((artist, genres_for_artist))

    with open("./data/artists_by_spotify_genres.csv", "w") as f:
        w = csv.writer(f)
        w.writerow(["artist", "genres"])
        for row in artists_by_genres:
            w.writerow([row[0], row[1]])
