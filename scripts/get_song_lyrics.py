from bs4 import BeautifulSoup
import config
import json
import pandas as pd
import requests

base_url = "http://api.genius.com"
headers = {"Authorization": "Bearer {}".format(config.GENIUS_CONFIG["CLIENT_ACCESS_TOKEN"])}

def get_song_info(artist, track):
    search_url = base_url + "/search"
    params = {"q": track}

    response = requests.get(search_url, params=params, headers=headers)
    json = response.json()

    song_info = None
    for hit in json["response"]["hits"]:
        if hit["result"]["primary_artist"]["name"] == artist:
            song_info = hit
            break

    return song_info

def lyrics_from_song_api_path(song_api_path):
    song_url = base_url + song_api_path
    response = requests.get(song_url, headers=headers)
    json = response.json()
    path = json["response"]["song"]["path"]

    page_url = "http://genius.com" + path
    response = requests.get(page_url)
    html = BeautifulSoup(response.text, "html5lib")
    [h.extract() for h in html("script")]
    lyrics = html.find("div", class_="lyrics").get_text().strip()

    return lyrics

if __name__ == "__main__":

    tracks_by_artist = pd.read_csv("./data/sample_tracks_by_artists_since_2013.csv")
    tracks_by_artist["lyrics"] = None

    for i, row in tracks_by_artist.iterrows():

        song_info = get_song_info(row["artist"], row["track"])

        if song_info:
            song_api_path = song_info["result"]["api_path"]
            lyrics = lyrics_from_song_api_path(song_api_path)
            tracks_by_artist.set_value(i,'lyrics',lyrics)
    
    tracks_by_artist.to_csv("./data/tracks_with_lyrics_since_2013.csv", index=False,)
