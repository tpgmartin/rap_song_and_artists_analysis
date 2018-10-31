from bs4 import BeautifulSoup
import csv
import re
import requests

# Need to handle artists which are
# * Various artists
# 

tracks_by_album_and_artist = []
with open('./data/charting_rap_albums_since_2017.csv') as f:
    reader = csv.reader(f)
    next(reader, None)
    
    for row in reader:

        artist = ('-').join(re.sub('[^0-9a-zA-Z\?\!]+',' ',row[0]).strip().split(' '))
        album = ('-').join(re.sub('[^0-9a-zA-Z\?\!]+',' ',row[1]).strip().split(' '))

        print("artist", artist)
        print("album", album)

        url = "https://genius.com/albums/{}/{}".format(artist, album)

        page = requests.get(url)
        html = BeautifulSoup(page.text, "html5lib")

        tracks = []
        for el in html.findAll("h3", {"class": "chart_row-content-title"}):
            track = []
            track.append(artist)
            track.append(album)
            track.append(el.find(text=True).strip())
            tracks.append(track)
        print('tracks')
        print(tracks)
        print('-------------------------')
        tracks_by_album_and_artist.extend(tracks)
        print('tracks_by_album_and_artist')
        print(tracks_by_album_and_artist)
        print('--------------------------')

with open("./data/tracks_by_artist_and_album.csv", "w") as f:
    w = csv.writer(f)
    w.writerow(["artist", "album", "track"])
    w.writerow([track for track in tracks_by_album_and_artist])