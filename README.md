# Rap Songs and Artists Analysis

This repo contains documents for my IN3061 / INM430 (Principles of Data Science) coursework assignment.

The HTML notebook can be viewed [here](https://smcse.city.ac.uk/student/aczd005/inm430_notebook.html)

## Scripts

### Get List of Artists

In order,

1. `get_charting_songs.py` find rap albums featured in Billboard Rap Album charts
2. `get_tracklist_for_albums.py` find track list for albums returned from above script
3. `filter_tracks_by_artists.py` for above tracks, find artists with at least 20 tracks where they are credited as sole featured artist
4. `get_song_lyrics.py` get song lyrics for filtered tracks


### Get Genres for Artists

Either,

* `get_genres.py` will scrape from Wikipedia
* `get_spotify_genres.py` will use Spotify API

### Other

* `create_google_form.py` generate random subset of artists for form
