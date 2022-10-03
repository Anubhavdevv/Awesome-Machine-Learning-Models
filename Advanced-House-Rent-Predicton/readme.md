# `Advanced House Rent Prediction`

This project aims to predict the rent of the houses of a certain location using the various features like size of the property, locality, BHK etc using Machine Learning Techniques.

We have followed lots of steps to do so. These steps are :

## 1. Installing and Importing libraries

- In the first step we have installed some libraries that we are going to use in our project. These are `Pandas`, `NumPy`, `Sklearn`, `Matplotlib` and `Sklearn`.

- These libaries have been imported in the .ipynb to use in the project.

## 2. Loading the Data and Getting the Info

- The second step starts with loading the .csv file in the project (both training and testing file) using pandas library.

- We checked the various info about the data using `.info()` and `.describe()` method and found that there are no null values and understood the various columns and analyse it as well and started `Feature Engineering`.

## 3. Feature Engineering

- Since there are no null values so it decreases the work a little bit.

- There are various columns that are not going to be useful for us like id, activation_date and amenities (as all the details of amenities are given in other columns) so dropped this columns.

- Then checked `correlation` of each column with others and found that floor and total_floor columns have a correlation of 71-72% so dropped total_floor columns as both are very much correlated.

- Afterwards we started moving on each column and find out that there are many `outliers` in our data which can affect the accuracy of our model so we dropped all those rows containing outliers.

- Transformed the '`type`' column from object data type to int by converting them into `bhk` column which contain numeric values like 1,2,3 etc.

- Then deal with the `locality` column at the last and found that the data contain information about houses from some locality various times but there are some locality whose information is very less. So we decided to put thos locality having less than 50 rows in '`other`' category which reduces the unique localities drastically.

- Till now we have cleaned each column and then split the dataset into inputs and target data.

- At last we breakdown the data into `training`, `testing` and `validation` dataset.

**We are ready to train the model now**

## 4. Training the Model

- Since this was a regression problem as we have to predict a continuous variable which is rent, so trained the model with different regression model and find out the best one.

- Created the pipeline which contains of two steps :

  1. Scaling the Numeric features and One Hot Encoding the Categorical Features
  2. Applying the Regression Model

- These Machine Learning regression Techniques are :

    1. Linear Regression
    2. Ridge and Lasso Regression
    3. Decision Tree Regression
    4. Random Forest Regression
    5. Gradient Boosting Regressor
    6. Adaboost Regressor
    6. K-Nearest Neighbors Regressor
    7. SVM-Regressor
    8. XgBoost Regressor
    9. Voting and Stacking Regressor

- Trained with each model and also tried various `hyperparameter tuning` techniques like changing depth of the tree, setting different learning rate etc.

- At last we found the best model suitable for our project which was `Gradient Boosting Regressor` which was giving the validation accuarcy of `82.51%`.

- Saved the pipeline in the pickle file.

## 5. Creating API Hosted Frontend Web File

- Created a `streamlit` web-app and deployed the model on `Heroku`

- Link of the Project : https://house-rent-predicter.herokuapp.com/

## THANK YOU
