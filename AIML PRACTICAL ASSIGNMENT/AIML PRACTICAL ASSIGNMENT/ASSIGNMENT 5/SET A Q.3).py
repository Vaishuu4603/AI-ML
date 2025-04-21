# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 19:45:00 2025

@author: jayes
"""
"""
import pandas as pd
from sklearn import linear_model
df=pd.read_csv("C:/Users/jayes/Downloads/minihomeprices.csv")
x=df[['area','bedrooms','age']]
y=df['price']

regr=linear_model.LinearRegression()
regr.fit(x,y)

predictedprice=regr.predict([[2000,3,10]])

print(predictedprice)
"""

import pandas as pd
from sklearn import linear_model
from sklearn.impute import SimpleImputer

# Load data
df = pd.read_csv("C:/Users/jayes/Downloads/minihomeprices.csv")

# Define features and target
x = df[['area', 'bedrooms', 'age']]
y = df['price']

# Handle missing values using mean imputation
imputer = SimpleImputer(strategy='mean')
x_imputed = imputer.fit_transform(x)

# Create and train the model
regr = linear_model.LinearRegression()
regr.fit(x_imputed, y)

# Predict with new data
predicted_price = regr.predict([[2000, 3, 10]])

print("Predicted price:", predicted_price[0])
