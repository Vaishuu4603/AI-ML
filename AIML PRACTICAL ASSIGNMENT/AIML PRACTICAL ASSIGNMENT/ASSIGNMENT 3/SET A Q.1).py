# -*- coding: utf-8 -*-
"""
Write a Python program to import necessary libraries to read a dataset and Describe the 
uses of Data Frame Attributes.(Use head(), tail(), shape, info() , describe() ,columns).
"""

import pandas as pd
df=pd.read_csv("C:/Users/jayes/Downloads/Dataset .csv")

print("first five rows")
print(df.head())

print("last five rows")
print(df.tail())

print("Dataset Information")
print(df.info())

print(" Dataset Summary")
print(df.describe())

print("Dataset Shape")
print(df.shape)

print("Dataset Colimn")
print(df.columns)













