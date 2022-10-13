
# LIVER DISEASE PREDICTION


![Logo](https://guires.uk/newsroom/wp-content/uploads/2019/11/Predicting-Liver-Disease.jpg)


## INTRODUCTION

We will use these patient records to determine which patients have liver disease and which ones do not. 
## CONTEXT

Patients with Liver disease have been continuously increasing because of excessive consumption of alcohol, inhale of harmful gases, intake of contaminated food, pickles and drugs. This dataset is used to evaluate prediction algorithms in an effort to reduce burden on doctors. 



## AIM

In this project, we are going to use the Indian Liver Patient Records dataset from kaggle and are going to predict whether a patient has liver disease or not based on certain features.

These features consist of total proteins,albumin etc whether it is asscoiated with disease or not.
## CONTENT

This data set contains 416 liver patient records and 167 non liver patient records collected from North East of Andhra Pradesh, India. The "Dataset" column is a class label used to divide groups into liver patient (liver disease) or not (no disease). This data set contains 441 male patient records and 142 female patient records.

Any patient whose age exceeded 89 is listed as being of age "90".

Columns:

   - Age of the patient
   - Gender of the patient
   - Total Bilirubin
   - Direct Bilirubin
   - Alkaline Phosphotase
   - Alamine Aminotransferase
   - Aspartate Aminotransferase
   - Total Protiens
   - Albumin
   - Albumin and Globulin Ratio
   - Dataset: field used to split the data into two sets (patient with liver disease, or no disease)


## APPROACH

First of all we have to import all the necessary libraries.
 
We will be checking all the null values for data cleaning purpose.

We will use a TensorFlow ANN to make our predictions and to build our model and at last, we will conclude our project with the accuracy of our model.


## CONCLUSION

We solved the problem with this approach 
(see the code for proper illustration).

Using TensorFlow, we achieve the best accuracy of our prediction system.