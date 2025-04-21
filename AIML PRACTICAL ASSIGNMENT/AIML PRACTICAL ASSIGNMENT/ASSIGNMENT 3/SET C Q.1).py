# -*- coding: utf-8 -*-
"""
1. Write a python program to implement 
Pre-Processing of Play_Tennis.csv DataSet.
● Import dataset & read a dataset.
● Handle the Missing Values
● Convert categorical data to numeric 
● Rescale/normalize the Data
● Split the dataset into a train & test
 set and print them.
"""

# 1. Import libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# 2. Load the dataset
df = pd.read_csv("C:/Users/jayes/Downloads/PlayTennis.csv")  # Replace with your correct path if needed
print(df.head())

# 3. Convert categorical columns to numeric using LabelEncoder
le = LabelEncoder()

df['Outlook'] = le.fit_transform(df['Outlook'])
df['Temperature'] = le.fit_transform(df['Temperature'])
df['Humidity'] = le.fit_transform(df['Humidity'])
df['Wind'] = le.fit_transform(df['Wind'])
df['Play Tennis'] = le.fit_transform(df['Play Tennis'])

# 4. Split dataset into features and target
X = df.iloc[:, :-1].values  # All columns except last
y = df.iloc[:, -1].values   # Last column

print("\nPreprocessed Data:\n", df)
print("\nFeatures (X):\n", X)
print("\nTarget (y):\n", y)
