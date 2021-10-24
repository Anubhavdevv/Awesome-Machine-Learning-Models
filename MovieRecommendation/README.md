<h1 align="center">👩‍⚕️ Movie Recommendation System</h1>

# ✅ Objective of this project
- The objective of this project is to recommend movies.
- We do content based filtering to recommend movies.

# 📚 Procedure :-
## ✔ Working on the dataset
- We get the column names and data shape.
- We perform exploratory data analysis 
- We plot Number of Viewers vs rating to conclude important subset fo data for making predictions. 
- We group the content by Title and Ratings
- We sort the ratings in descending order

## ✔ Build recommendation model for one movie
- We get ratings for one movie and put it into a new dataframe
- Now we make a correlation matrix between new dataframe and movie matrix
- We arrange the movie matrix in descending order on the basis of correlation score
- The most correlated movies show up on top

## ✔ Generalize the model for all the movies now
- We input movie name from user
- We make the correlation matrix
- We sort the correlation score in descending order
- Our prediction are ready. 

