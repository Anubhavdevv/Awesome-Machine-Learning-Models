# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 01:35:57 2023

@author: user
"""

import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('D:\placement/MINOR/trained_model 1.sav' , 'rb'))

# input data
input_data = [2,0,70, 75 ,6 ,8, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# convert input data to numpy array
input_data_np = np.array(input_data).reshape(1, -1)

# make prediction
prediction = loaded_model.predict(input_data_np)
print(prediction)

# print result
if prediction[0] == 0:
    print("The student is not placed.")
else:
    print("The student is placed!")