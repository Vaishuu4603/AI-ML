# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 21:27:39 2025

@author: jayes
"""

import pandas as pd
import numpy as np
df=pd.read_csv("C:/Users/jayes/Downloads/diabetes.csv")
df.head()
x=df.iloc[:,:-1].values
y=df.iloc[:,4].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
dtree=DecisionTreeClassifier()
dtree=dtree.fit(x,y)
y_pred=dtree.predict(x_test)
dtree.predict([[6,148,72,35,0,33.6,0.627,50]])
print(y_pred)