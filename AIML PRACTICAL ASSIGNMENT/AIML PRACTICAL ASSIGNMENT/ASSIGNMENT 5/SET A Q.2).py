# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 19:24:12 2025

@author: jayes
"""
"""
import pandas as pd
from sklearn import linear_model
df=pd.read_csv("C:/Users/jayes/Downloads/Book1.csv")
#df = pd.read_csv('C:/Users/jayes/Downloads/car_data.xlsx', encoding='latin1')
x=df[['Weight','Volume']]
y=df['CO2']
regr=linear_model.LinearRegression()
regr.fit(x,y)

predictCO2=regr.predict([[2300,1300]])
print(predictCO2)

"""
import pandas as pd
from sklearn import linear_model

# Load the CSV file
df = pd.read_csv("C:/Users/jayes/Downloads/Book1.csv")

# Drop rows where 'CO2' is NaN
df = df.dropna(subset=['CO2'])

# Select features and target
x = df[['Weight', 'Volume']]
y = df['CO2']

# Train the model
regr = linear_model.LinearRegression()
regr.fit(x, y)

# Predict CO2 for given Weight and Volume
predictCO2 = regr.predict([[2300, 1300]])

print("Predicted CO2 emission:", predictCO2[0])
