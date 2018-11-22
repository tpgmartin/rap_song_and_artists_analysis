import billboard
import csv
from datetime import date, datetime, timedelta

def get_chart_entries(playlist, dates):
    ret = []
    delta = timedelta(days = 0)
    for date in dates:
        if date > datetime.today().date():
            continue
        chart = billboard.ChartData(playlist, str(date + delta))
        ret.append(chart)
    return ret

def get_songs_by_artists(charts):
    d = {}

    for chart in charts:
        for song in chart.entries:
            key = song.artist
            if key not in d:
                d[key] = []
            if song.title not in d[key]:
                d[key].append(song.title)

    return d

def main():

    dates = [date(year = year, month = month, day = 1) for month in range(1,13) for year in range(2013,2019)]

    charts = get_chart_entries("rap-albums", dates)
	
    songs_by_artists = get_songs_by_artists(charts)

    with open("./data/charting_rap_albums_since_2013.csv", "w") as f:
        w = csv.writer(f)
        w.writerow(["artist", "album"])
        for artist, albums in songs_by_artists.items():
            for album in albums:
                w.writerow([artist, album])

if __name__ == "__main__":
    main()

