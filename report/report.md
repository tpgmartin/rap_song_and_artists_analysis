# Classification of Rap Artists by Lyrics
## INM430 Coursework
Thomas Martin
16th December 2018

Total 500 words

## I. Introduction

### Domain

This project aims to create a model to accurately classify tracks by  artists using their lyrics (or features generated from their lyrics) alone. Analysis of song lyrics is a popular research topic as they form an interesting area of natural language processing (NLP) research, as they have characteristics different to prose such as a greater emphasis on rhyme, structure, and repetition.

Research tends to focus on one of two tasks,

* Supervised: can songs be accurately categorised by a given piece of metadata e.g. artist
* Unsupervised: can the relationship between songs be characterised by a given piece of metadata e.g. genre

### Related Work

This paper is falls into the former category. In the supervised domain there have been a number of attempts to classify song lyrics at the level of artist, release period, or genre. In all cases the

Classifiers typically used include logistic

However, previous studies do not generally limit themselves by both music genre and release date 

In general, previous work has used lyrics for the purpose of 

Frequently follows an unsupervised task resulting in classification of artists

Michael Fell and Caroline Sporleder. 2014. "Lyrics-based Analysis and Classification of Music." Proceedings of COLING 2014, the 25th International Conference on Computational Linguistics: Technical Papers, pp.620–631

### Questions

This project will specifically address the following questions,

1. Can the model match the reported results of other authors?
2. How does the choice between text representation affect the accuracy of the model and why?
3. How does the choice between classifier affect the accuracy of the model any why?
4. Are some artists 

List of objectives

* Accurately classify song by artist using lyrics
* Effectiveness of word embeddings vs bag-of-words
* Find set of (derived?) features for an effective classifier
* Get comparable performance to benchmark


## II. Approach

### Data Collection

Due to [legal issues](https://genius.com/discussions/277279-Get-the-lyrics-of-a-song) surrounding the use and distribution of lyrics ... 

The data for this project was taken from a couple websites. To find the set of relevant artists, the script `get_charting_albums.py` finds all albums to have featured on the Billboard Rap Albums chart between January 2000 and November 2018. From this, I wanted to find a set of the top 10 most prolific artists in this time period (why???). To do this I found the full track list for each album with `get_tracklist_for_albums.py`, and grouped the total number of released tracks by artist. For these ten artists, I found the matching lyrics for each song from [Genius.com](https://genius.com/) using `get_song_lyrics.py`. This set of lyrics was further refined as not all lyrics were successfully returned from the website following this procedure due to parsing errors. In total, the lyrics 679 tracks for 10 artists were found. 

![Total number of tracks with lyrics by artist](./report/total_number_of_tracks_by_artist.png "Total number of tracks with lyrics by artist")

The number of tracks for artist ranged from 39 for E-40, to 101 for Eminem

All scripts for the data collection process are in the `scripts` folder.

### Analysis Strategy

With a data collected, I planned to do the following,

* Pre-process the lyrics following typical NLP techniques. Using Sklearn 

As part of the pre-processing process, I needed to go through a process of feature engineering

Features considered for each track

* Song vectors
* Total line count
* Average line length
* Unique word proportion

To get the raw text data into a usable format I used one of the following processes to get the lyrics into a vector format.

* TF-IDF on the raw lyrics
* TF-IDF after POS-tagging of the raw lyrics
* Doc2Vec

Following the approach of other papers on this topic, I will use the following classifier for the final model,

* Logistic regression,
* SVM,
* Naive Bayes. (for naive bayes need to set doc2vec to particular setting)

(Why???)

http://billchambers.me/tutorials/2015/01/14/python-nlp-cheatsheet-nltk-scikit-learn.html


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


Total 1000 words
## III. Analysis of Results

### Analysis

Link to html computation notebook ... 

The evaluation metrics I will use are,

* Precision: the proportion of correctly classified elements for a given class, out of all the data points predicted for that class
* Recall: the proportion of correctly classified elements for a given class, out of all the relevant data points for that class
* F-Measure: a weighted average of precision and recall, over all classes.

These are typically used for tasks such as this that deal with an unbalanced, multi-class classification problems. This is because they do a job of indicating how well a model identifies true positives, while keeping false positives and false negatives to a minimum.

A big part of of this project is to compare the performance of different text representations for the classification task. The text representations considered were,

* Bag-of-Words: This is the simplest text representation considered, ... 
* TF-IDF
* Doc2Vec

Discuss differences between logistic regression and SVM


TF-IDF Representation - also include hyperparameters

| Classifier          | Precision | Recall | F Measure |
| ------------------- | --------- | ------ | --------- |
| Logistic Regression | %     | %  | %     |
| Linear SVC          | %     | %  | %     |

Doc2Vec Representation - also include hyperparameters

| Classifier          | Precision | Recall | F Measure |
| ------------------- | --------- | ------ | --------- |
| Logistic Regression |           |        |           |
| Linear SVC          |           |        |           |

Best performing classifier by text representation

| Text Representation | Classifier          | Precision | Recall   | F Measure |
| ------------------- | ------------------- | --------- | -------- | --------- |
| Bag-of-Words        | Logistic Regression | 73.0%     | 72.5.6%  | 72.0%     |
| TF-IDF              | Linear SVC          |           |          |           |
| Doc2Vec             | Linear SVC          |           |          |           |


## IV. Conclusions

### Reflections

Given the data collection process for this project, there are some concerns as to the direct reproducibility of this study. Discussed above, the lyrics were taken from a third-party website and assume a standard format for the convenience of the web scraper script. In addition, as the lyrics are entered via user submission they are not necessarily reliable in their content or format. Relatedly, although the tracks investigated were chosen specifically because only the target artists was credited as the featured artists, there were a number of instances of other artists appearing on the track without credit.

* Dataset contained unbalanced classes - is this evident in wrongly classified artists?
* Overall size of dataset may be an issue?
* Not directly comparable to benchmarks due to scope of study: just one genre, only songs from 2000
* What features were not considered? Is this important? Why/why not?
* Only considered unigrams

Relate to original objectives and motivations

I believe this project has shown the efficacy of classifying artists by their written lyrics alone. From a business perspective, this has utility in forming the foundation of a text based search engine for a music index. This could also form a component of a music recommendation system, with suggestions based on the similarity of lyrical content between artists.

## V. References

* http://cs229.stanford.edu/proj2013/CS229FinalPaper.pdf
* https://publik.tuwien.ac.at/files/PubDat_166272.pdf
