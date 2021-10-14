# Sentiment Analysis for Restaurant Reviews

The goal of this problem statement is to analyze and build a prediction model to predict whether a review on the restaurant is positive or negative.
Performing Sentiment Analysis on the restaurant reviews to find out if the review is good or bad. Also to apply dimensionality reduction to reduce the number of parameters.


**Dataset:** https://www.kaggle.com/hj5992/restaurantreviews <br> 
Reviews.tsv is a Kaggle dataset which consists of 1000 reviews on a restaurant.

To build a model to predict if review is positive or negative, following pipeline is used.

1. Preprocessing Dataset <br>
a. Remove stopwords and clean text <br>
b. Stemming or Lemmatization 
2. Count Vectorization for creating a Bag of Words model
3. Training and Classification with many parameters without reducing Parameter Dimensionality
4. Applying feature scaling along with Dimensionality Reduction using: <br>
a. Principal Component Analysis <br>
b. Linear Discriminant Analysis
5. Training and Classification after Dimensionality Reduction 
6. Analysis Conclusion
