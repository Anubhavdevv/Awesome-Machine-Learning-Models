<h1 align="center"> 👩‍⚕️ Diabetes Classification </h1>

 # Objective 
- The project aims to predict if a person is suffering from diabetes on the basis of information given in data.
- The independent variables in this data set are :-'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age'
- The outcome variable value is either 1 or 0 indicating if a person has diabetes or not.

# Algorithm/Classifiers used:- 
### K-nearest neighbor
K-nearest neighbor is a non-parametric algorithm that classifies data points based on their proximity and association to other available data. This algorithm assumes that similar data points can be found near each other. As a result, it seeks to calculate the distance between data points and assigns a category based on the most frequent category or average.
### Multi-Layer Perceptron (MLP)
A multilayer perceptron (MLP) is a feedforward artificial neural network that generates a set of outputs from a set of inputs. An MLP is characterized by several layers of input nodes connected as a directed graph between the input and output layers. MLP uses backpropogation for training the network. MLP is a deep learning method.
### Light GBM 
It is a gradient boosting framework that makes use of tree based learning algorithms. LightGBM algorithm grows vertically meaning it grows leaf-wise. LightGBM chooses the leaf with large loss to grow. It can lower down more loss than a level wise algorithm when growing the same leaf.
### SVM
A support vector machine (SVM) is machine learning algorithm that analyzes data for classification and regression analysis. SVM is a supervised learning method that looks at data and sorts it into one of two categories. An SVM outputs a map of the sorted data with the margins between the two as far apart as possible. 
### Logistic Regression
Logistic Regression is a Machine Learning algorithm which is used for the classification problems, it is a predictive analysis algorithm and based on the concept of probability. It uses a more complex function known as Sigmoid Function.
### Random Forest 
Random forests or random decision forests are an ensemble learning method for classification, regression and other tasks that operates by constructing a multitude of decision trees at training time.

## Summary  
The distribution of data was studied before preprocessing it by standard scaler. All the listed classifiers were implemented along with different parameters based on their cross validation score. The accuracies were studied and it was concluded that Random Forest gave the best accuracy.

