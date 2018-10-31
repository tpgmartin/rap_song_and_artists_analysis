from bs4 import BeautifulSoup
import csv
import re
import requests

tracks_by_album_and_artist = []
with open('./data/charting_rap_albums_since_2017.csv') as f:
    reader = csv.reader(f)
    next(reader, None)
    
    for row in reader:

        artist = row[0]
        album = row[1]

        formatted_artist = ('-').join(re.sub('[^0-9a-zA-Z\?\!]+',' ',artist).strip().split(' '))
        formatted_album = ('-').join(re.sub('[^0-9a-zA-Z\?\!]+',' ',album).strip().split(' '))

        url = "https://genius.com/albums/{}/{}".format(formatted_artist, formatted_album)

        tracks = []
        response = requests.get(url)
        if response.status_code == 404:
            track = []
            track.append(artist)
            track.append(album)
            tracks.append(track)
        else:
            html = BeautifulSoup(response.text, "html5lib")
            for el in html.findAll("h3", {"class": "chart_row-content-title"}):
                track = []
                track.append(artist)
                track.append(album)
                track.append(el.find(text=True).strip())
                tracks.append(track)
        tracks_by_album_and_artist.extend(tracks)

with open("./data/tracks_by_artist_and_album.csv", "w") as f:
    w = csv.writer(f)
    w.writerow(["artist", "album", "track"])
    for track in tracks_by_album_and_artist:
        w.writerow(track)