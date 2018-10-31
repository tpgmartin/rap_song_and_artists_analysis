import csv

target_artists = []
with open('./data/target_artists.csv') as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        target_artists.append(row[0])

with open('./data/target_artists.csv') as f:
    reader = csv.reader(f)
# filter out "Ft.""
# J. Cole,4 Your Eyez Only,4 Your Eyez Only [Credits]
# J. Cole,4 Your Eyez Only,4 Your Eyez Only [Tracklist + Album Art]
# J. Cole,2014 Forest Hills Drive,2014 Forest Hills Drive [Album Art + Tracklist]
# J. Cole,4 Your Eyez Only,4 Your Eyez Only [Booklet]
# [Tracklist + Album Cover]