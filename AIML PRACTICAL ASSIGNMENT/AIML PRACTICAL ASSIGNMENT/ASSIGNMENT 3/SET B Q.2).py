# -*- coding: utf-8 -*-
"""
Write a python program to implement Data Splitting: Split the given dataset into train set 
and test set which is of 70% & 30% respectively and print them.[use any dataset]
"""

import pandas as pd
from sklearn.model_selection import train_test_split
df=pd.read_csv("C:/Users/jayes/Downloads/Salary_Data.csv")

print(df)
print("Spliting your data in x and y variable")
x=df.iloc[:,:-1]
print(x)

y=df.iloc[:,1]
print(y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
print(x_train)
print(x_test)
print(y_train)
print(y_test)







