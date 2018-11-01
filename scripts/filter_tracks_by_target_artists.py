import csv
import pandas as pd

target_artists = []
with open('./data/target_artists.csv') as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        target_artists.append(row[0])

tracks_by_artist_and_album = pd.read_csv("./data/tracks_by_artist_and_album.csv")

filtered_tracks_by_artist_and_album = tracks_by_artist_and_album[tracks_by_artist_and_album["artist"].isin(target_artists)]
filtered_tracks_by_artist_and_album = filtered_tracks_by_artist_and_album[~filtered_tracks_by_artist_and_album["track"].str.contains("Ft.",regex=False)]
filtered_tracks_by_artist_and_album = filtered_tracks_by_artist_and_album[~filtered_tracks_by_artist_and_album["track"].str.contains("[",regex=False)]

grouped = filtered_tracks_by_artist_and_album.groupby(["artist"]).agg("count")
grouped.reset_index(inplace=True)
grouped = grouped[grouped["track"] > 19]

tracks_by_artist_at_least_20 = filtered_tracks_by_artist_and_album[filtered_tracks_by_artist_and_album["artist"].isin(grouped["artist"].values)]

grouped_at_least_20 = tracks_by_artist_at_least_20.groupby(["artist"], group_keys=False)

sample_tracks_by_artist = grouped_at_least_20.apply(lambda x: x.sample(n=20))
sample_tracks_by_artist.sort_values(by=["artist"],inplace=True)
sample_tracks_by_artist = sample_tracks_by_artist[["artist", "album", "track"]]

sample_tracks_by_artist.to_csv("./data/sample_tracks_by_artists.csv", index=False,)