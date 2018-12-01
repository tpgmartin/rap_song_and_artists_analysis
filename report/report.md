# Classification of Rap Artists by Lyrics Analysis
## INM430 Coursework
Thomas Martin
16th December 2018

Total 500 words
## I. Introduction

Analysis of domain

* Why lyrics?
* Why rap artists?
* Related literature

Questions

* List of analytical questions to tackle

List of objectives

* Accurately classify song by artist using lyrics
* Effectiveness of word embeddings vs bag-of-words
* Find set of (derived?) features for an effective classifier
* Get comparable performance to benchmark

Other data exploration points
* Differences by year?
* Differences by location?
* Differences by sub-genre?

### Related Work

Analysis of lyrics has proved to be a powerful analytical tool in the classification of songs at the level of artist, genre, and release date.

Lyrics only

Classifiers typically used include logistic

However, previous studies do not generally limit themselves by both music genre and release date 

In general, previous work has used lyrics for the purpose of 

Frequently follows an unsupervised task resulting in classification of artists

Michael Fell and Caroline Sporleder. 2014. "Lyrics-based Analysis and Classification of Music." Proceedings of COLING 2014, the 25th International Conference on Computational Linguistics: Technical Papers, pp.620–631

## II. Approach

Discuss analysis strategy

Plan

### Data Collection

Although tasks similar to the one presented in this paper have been performed before, due to intellectual property restrictions around the ownership of an artist’s lyrics, no ready data dump was available for this investigation. Consequently, I choose to gather my own data in the following process,

1. Find all charting Rap albums since 2000 from Billboard Rap Albums charts
2. Find track listing for these charting albums by making requests to Genius `/albums` url
3. For the total set of tracks for these charting albums, find the top 10 most prolific artists by tracks
4. For this subset of tracks for the most prolific artists, filter out track results that are either not audible songs e.g. Album Artwork, or where it is not a solo-feature
5. Then find the lyrics for all these artists’ tracks by again making request to Genius
6. (Not all of these songs were 

This five step process resulted in a set of of raw lyrics for 756 tracks, which needed to be preprocess before they could be used to train the models.

### Data Preprocessing

Normalisation includes
* Standardise casing
* Removal of whitespace
* Removal of punctuation
* Removal of stopwords
* (Did not perform lemmatisation - why?)

Vectorisation
* TF-IDF
* Doc2Vec

Other feature engineering


Why choice of models

Link to html computation notebook ... 

### Data Collection

Total 1000 words
## III. Analysis of Results

### Analysis

Evaluation metrics
* Accuracy
* Precision
* Recall
* F Measure

For best performing classifier produce confusion matrix for test results


## Conclusions

### Reflections

* Dataset contained unbalanced classes - is this evident in wrongly classified artists?
* Overall size of dataset may be an issue?
* Problems with lyrics collected?
    - User entered text - not necessarily reliable
    - Inconsistencies in text format
    - Song lyrics may also include other 
* Not directly comparable to benchmarks due to scope of study: just one genre, only songs from 2000
* What features were not considered? Is this important? Why/why not?
* Reproducibility of study due to availability of data set

Relate to original objectives and motivations

## References