import billboard
from datetime import date, datetime, timedelta
import json

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

    dates = [date(year = year, month = month, day = 1) for month in range(1,13) for year in range(2010,2019)]

    charts = get_chart_entries("hot-100", dates)
	
    songs_by_artists = get_songs_by_artists(charts)

    with open("songs_by_artists_since_2010.json", "w") as outfile:
        json.dump(songs_by_artists, outfile, sort_keys=True, indent=4)

    


if __name__ == "__main__":
    main()

