import config
import json
import requests

# song_titles = []
# with open('./data/songs_by_artists_since_2010.json') as data:
#     d = json.load(data)
#     for artist, song_title in d.items():
#         song_titles.extend(song_title)

artist = "A Boogie Wit da Hoodie Featuring Kodak Black"
song_title = "Drowning"

if __name__ == "__main__":
    url = "http://api.genius.com/search"
    headers = {"Authorization": "Bearer {}".format(config.GENIUS_CONFIG["CLIENT_ACCESS_TOKEN"])}

    params = {"q": song_title}
    response = requests.get(url, params=params, headers=headers)
    json = response.json()
    song_info = None
    for hit in json["response"]["hits"]:
        print(hit["result"]["primary_artist"]["name"])
        if hit["result"]["primary_artist"]["name"] == artist:
            song_info = hit
            break
    if song_info:
        song_api_path = song_info["result"]["api_path"]
        print(lyrics_from_song_api_path(song_api_path))