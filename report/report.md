# Classification of Rap Artists by Lyrics
## INM430 Coursework
Thomas Martin
16th December 2018

## I. Introduction

### Domain

This project aims to create a model to accurately classify tracks by  artists using their lyrics (or features generated from their lyrics) alone. Analysis of song lyrics is a popular research topic as they form an interesting area of natural language processing (NLP) research, as they have characteristics different to prose such as a greater emphasis on rhyme, structure, and repetition.

Research tends to focus on one of two tasks,

* Supervised: can songs be accurately categorised by a given piece of metadata e.g. artist
* Unsupervised: can the relationship between songs be characterised by a given piece of metadata e.g. genre

### Related Work

This paper is falls into the former category. In the supervised domain there have been a number of attempts to classify song lyrics at the level of artist, release period, or genre. In all cases the

Classifiers typically used include logistic regression 

However, previous studies do not generally limit themselves by both music genre and release date as this project does.

Frequently follows an unsupervised task resulting in classification of artists

### Questions

This project will specifically explore the following questions,

1. Can the model match the reported results of other authors?
2. How does the choice between text representation affect the accuracy of the model?
3. How does the choice between classifier affect the accuracy of the model?

List of objectives

* Accurately classify song by artist using lyrics
* Effectiveness of word embeddings vs bag-of-words
* Find set of (derived?) features for an effective classifier
* Get comparable performance to benchmark


## II. Approach

### Data Collection

The data for this project was taken from a couple websites. To find the set of relevant artists, the script `get_charting_albums.py` finds all albums to have featured on the Billboard Rap Albums chart between January 2000 and November 2018. From this, I wanted to find a set of the top 10 most prolific artists in this time period, this is simply to ensure that I have sufficient number of tracks for each artist. To do this I found the full track list for each album with `get_tracklist_for_albums.py`, and grouped the total number of released tracks by artist. For these ten artists, I found the matching lyrics for each song from [Genius.com](https://genius.com/) using `get_song_lyrics.py`. This set of lyrics was further refined as not all lyrics were successfully returned from the website following this procedure due to parsing errors (In the notebook, I filter out row from the dataframe with null lyrics). In total, the lyrics 679 tracks for 10 artists were found.

![Total number of tracks with lyrics by artist](./report/total_number_of_tracks_by_artist.png "Total number of tracks with lyrics by artist")

The number of tracks for artist ranged from 39 for E-40, to 101 for Eminem

All scripts for the data collection process are in the `scripts` folder.

### Analysis Strategy

With a data collected, I planned to do the following,

* Pre-process the lyrics following typical NLP techniques.

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
* Removal of stopwords

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
* Recall: the proportion of correctly classified elements for a given class, out of all the relevant data points for that class from the training data
* F-Measure: a weighted average of precision and recall, over all classes.

These are typically used for tasks such as this that deal with an unbalanced, multi-class classification problems. This is because they do a job of indicating how well a model identifies true positives, while keeping false positives and false negatives to a minimum.

A big part of of this project is to compare the performance of different text representations for the classification task. The text representations considered were,

* Bag-of-Words (BOW): This is the simplest text representation considered. Each track is represented by a vector where each value of the vector is the frequency of each token identified from the source text.  
* TF-IDF: Short for text frequency-inverse document frequency. This weights the BOW representation by the inverse frequency with which a given token appears in a given track. This means that tokens that are frequently found across all tracks are penalised, whereas tokens found in only a few tracks are promoted.
* Doc2Vec: This approach tries to predict a given word in a track using both the set of surrounding words as well as the document feature vector. This representation learns both syntactic and semantic meaning of tokens.

Discuss differences between logistic regression and SVM ... 

For both TF-IDF and Doc2Vec we see an improvement over the BOW approach by around 7% across all evaluation metrics, and see almost identical performance between the former two. The difference between the text representations is potentially even smaller still if we were to consider the same classifier - for instance see the performance against the test set.

| Text Representation | Classifier          | Precision | Recall   | F Measure |
| ------------------- | ------------------- | --------- | -------- | --------- |
| BOW                 | Logistic Regression | 72.3%     | 71.1%  | 70.7%     |
| TF-IDF              | Linear SVC          | 78.8%     | 77.9%    | 77.4%     |
| Doc2Vec             | Linear SVC          | 75.6%     | 75.0%    | 74.6%     |

The small differences between the results indicate that BOW characterises the tracks well enough. To compare with TF-IDF, we see that the BOW vectors have a dimensionality of 15,593 whereas TF-IDF vectors are of 15,578 as the 30% most frequent tokens were dropped. In both cases this indicates a large degree of linear independence between the feature space of the extracted tokens. This is probably joint result result of not stemming tokens, as well as not filtering out infrequently occurring tokens. To give an example, vocalisations related to "ah" appeared the tokens "ah", "ah-ahh", "ah-em", "aha", "ahah", "ahahah", "ahh", "ahhh", "ahhhh", "ahhhhh", "ahhhhhhh". The small improvement of TF-IDF over BOW may be due to the feature scaling that the former introduces: BOW frequencies can be scaled to close to zero, aiding the classification process, without changing the dimensionality of the feature space.

The full results for the model using the Doc2Vec text representation are reproduced below.

![Confusion Matrix for classifier using Doc2Vec text representation](./report/confusion_matrix.png "Confusion Matrix for classifier using Doc2Vec text representation")

For both text pr

Test set accuracy for Doc2Vec 79.6% vs 76.8%

The follow

#### Doc2Vec

| Artist      | Precision | Recall | F-Measure | Support |
| ----------- | --------- | ------ | --------- | ------- |
| Rick Ross   | 74%      | 89%   |   81%    |    28   |
|  Gucci Mane | 78%      | 58%   |   67%    |    12   |
|    The Game | 90%      | 93%   |   92%    |    30   |
|        T.I. | 88%      | 85%   |   86%    |    26   |
|      Eminem | 63%      | 55%   |   59%    |    22   |
|   Tech N9ne | 80%      | 62%   |   70%    |    13   |
|        E-40 | 71%      | 62%   |   67%    |    16   |
|       Drake | 76%      | 90%   |   83%    |    21   |
|   Lil Wayne | 54%      | 68%   |   60%    |    22   |
|  Snoop Dogg | 78%      | 50%   |   61%    |    14   |

#### TF-IDF

| Artist      | Precision | Recall | F-Measure | Support |
| ----------- | --------- | ------ | --------- | ------- |
| Rick Ross   |  69%      | 96%    | 81%       | 28      |
|  Gucci Mane |  78%      | 58%    | 67%       | 12      |
|    The Game |  90%      | 90%    | 90%       | 30      |
|        T.I. |  89%      | 92%    | 91%       | 26      |
|      Eminem |  65%      | 59%    | 62%       | 22      |
|   Tech N9ne |  75%      | 69%    | 72%       | 13      |
|        E-40 |  79%      | 69%    | 73%       | 16      |
|       Drake |  70%      | 90%    | 79%       | 21      |
|   Lil Wayne |  82%      | 64%    | 72%       | 22      |
|  Snoop Dogg |  89%      | 57%    | 70%       | 14      |

We see that precision and recall are, in general, not always in agreement with each other, for instance Rick Ross has a below average precision but above average recall, and the opposite is the case for Lil Wayne. This means that for an artist like Rick Ross, the model did a good job of correctly classifying tracks to him, but also attributed more tracks from other artists to him as well. For Lil Wayne, the model frequently attributed his songs to other artists. This can be seen in the off-diagonal elements of the confusion matrix. Due to these differences in precision and recall, it could be argued that the model was biased towards some artists more than others. However, this does not seems to be due to support i.e. the number of tracks by artist in the test set, but rather may have implications for the text representation.

Comparing between text representation, the classifications were highly correlated. Considering f-measure only, this has Pearson correlation coefficient of 0.92 and p-value of 0.0002, meaning that there is a large, positive correlation between the two sets of results, which is statistically significant. It's hard to characterise the differences between the two approaches considered. However looking at artists known for there song structure and technical such as Eminem we find Doc2Vec outperforms TF-IDF, f-measure of 67% vs 55%, whereas artists better known for neologism and ad-libs such as Gucci Mane are better classified by TF-IDF.

Below, we see that the standard deviation for precision for TF-IDF is almost twice that of Doc2Vec, meaning the latter produces more consistent results on average. This also has implication for the f-measure, as f-measure is calculated from precision and recall.

#### Mean and Standard Deviation for each metric

| Text Representation | Precision | Recall   | F-Measure |
| ------------------- | --------- | -------- | --------- |
| TF-IDF              | 79%±9.0%   | 78%±15%  | 77%±9.5%   |
| Doc2Vec             | 76%±11%  | 75%±16%  | 75%±12%    |

The results obtained in this project are in the range reported by other authors. For instance, [1] reports f-measures of 52% and 91% for a logistic regression and naive bayes model respectively. Other authors report accuracy only, so are difficult to directly compare, but [2] reports an accuracy around 70% for a smaller set of only five artists.

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

Adding more documents to the dataset will not necessarily aid the classifier

## V. References

1. Hussein Hirjee and Daneil G. Brown. 2010 "Using Automated Rhyme Detection to Characterize Rhyming Style in Rap Music" Empirical Musicology Review, pp.121-145
2. Adam Sadovsky and Xing Chen "Song Genre and Artist Classification via Supervised Learning from Lyrics" CS 224N Final Project