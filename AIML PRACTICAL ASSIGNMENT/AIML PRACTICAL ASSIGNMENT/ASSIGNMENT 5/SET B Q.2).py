# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 20:46:56 2025

@author: jayes
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
dataset = pd.read_csv("C:/Users/jayes/Downloads/Social_Network_Ads.csv")

# Extract features and target
x = dataset.iloc[:, [2, 3]].values  # Age and EstimatedSalary
y = dataset.iloc[:, 4].values      # Purchased (0 or 1)


#optional code
from sklearn.model_selection import train_test_split
x_train , x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
y_test=sc.transform(x_test)

# Train the Naive Bayes classifier
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
#classifier.fit(x_train,y_train)
classifier.fit(x, y)

#y_pred=classifier.predict(x_test)

# Predict for new data [Age=48, Salary=75000] → Must be 2D
y_pred = classifier.predict([[48, 75000]])

print("Prediction for [48, 75000]:", y_pred[0])
