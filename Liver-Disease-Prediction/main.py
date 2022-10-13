# -*- coding: utf-8 -*-
"""Liver Disease Prediction using TensorFlow

#Getting Started

**Importing necessary libraries**
"""

import numpy as np
import pandas as pd
import plotly.express as px

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import tensorflow as tf

"""**Reading the dataset**"""

data = pd.read_csv('indian_liver_patient.csv')
data

data.info()

"""#Preprocessing
**Missing Values**
"""

data.isna().sum()

data['Albumin_and_Globulin_Ratio'] = data['Albumin_and_Globulin_Ratio'].fillna(data['Albumin_and_Globulin_Ratio'].mean())

"""**Encoding**"""

def binary_encode(df, column, positive_value):
    df = df.copy()
    df[column] = df[column].apply(lambda x: 1 if x == positive_value else 0)
    return df

data = binary_encode(data, 'Gender', 'Male')

data = binary_encode(data, 'Dataset', 1)

"""**Splitting and Scaling**"""

data

y = data['Dataset']
X = data.drop('Dataset', axis=1)

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)

"""**Training**"""

X.shape

y.sum() / len(y)

inputs = tf.keras.Input(shape=(10,))
x = tf.keras.layers.Dense(64, activation='relu')(inputs)
x = tf.keras.layers.Dense(64, activation='relu')(x)
outputs = tf.keras.layers.Dense(1, activation='sigmoid')(x)

model = tf.keras.Model(inputs=inputs, outputs=outputs)


model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=[
        'accuracy',
        tf.keras.metrics.AUC(name='auc')
    ]
)


batch_size = 64
epochs = 31

history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    batch_size=batch_size,
    epochs=epochs,
    verbose=0
)

"""**Results**"""

fig = px.line(
    history.history,
    y=['loss', 'val_loss'],
    labels={'index': "Epoch", 'value': "Loss"},
    title="Training and Validation Loss"
)

fig.show()

np.argmin(history.history['val_loss']) + 1

"""**Accuracy**"""

model.evaluate(X_test, y_test)