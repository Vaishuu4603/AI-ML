# -*- coding: utf-8 -*-
"""
Write a Program to implement Data cleaning -find all null values/missing values in a 
given dataset and remove them. [use any dataset]
"""

import pandas as pd
df=pd.read_csv("C:/Users/jayes/Downloads/airquality.csv")

print(df)
print("Data set is null")
df.isnull()
df.isnull().head(10)
df.isnull().tail(10)

print(" Display all null values sum")
df.isnull().sum()

df.isnull().head(50).sum()

print("replace all null values with specific symbol")
modifiyedDataset=df.fillna('*')

print("count the null values from modifiyed dataset")
modifiyedDataset.isnull().sum()

print("remove all null values")
df.dropna()









