import config
import csv
import requests
import pandas as pd

base_url = "https://api.spotify.com/v1/search"

def get_release_date_for_album(album):

    querystring = {
        "q": album,
        "type": "album"
    }

    headers = { 'Authorization': "Bearer {}".format(config.SPOTIFY_CONFIG["BEARER_TOKEN"]) }

    response = requests.request("GET", base_url, headers=headers, params=querystring)

    try:
        return response.json()["albums"]["items"][0]["release_date"]
    except:
        print(album)

if __name__ == "__main__":

    albums = pd.read_csv("./data/sample_tracks_by_artists_since_2013.csv")["album"].unique()

    album_by_release_date = []
    for album in albums:
        release_date = get_release_date_for_album(album)
        album_by_release_date.append((album, release_date))

    with open("./data/albums_with_release_date.csv", "w") as f:
        w = csv.writer(f)
        w.writerow(["album", "release_date"])
        for row in album_by_release_date:
            w.writerow([row[0], row[1]])
