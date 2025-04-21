# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 20:08:45 2025

@author: jayes
"""

import numpy as np
import pandas as pd

data=pd.read_csv("C:/Users/jayes/Downloads/PlayTennis.csv")

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

data['Outlook']=le.fit_transform(data['Outlook'])
data['Temperature']=le.fit_transform(data['Temperature'])
data['Humidity']=le.fit_transform(data['Humidity'])
data['Wind']=le.fit_transform(data['Wind'])
data['Play Tennis']=le.fit_transform(data['Play Tennis'])

x=data.iloc[:,:-1].values
y=data.iloc[:,4].values

from sklearn import tree
Clf = tree.DecisionTreeClassifier(criterion='entropy')
clf=Clf.fit(x,y)

tree.plot_tree(clf)
x_pred=clf.fit(x,y)

tree.plot_tree(clf)
x_pred=clf.predict(x)
x_pred==y
# Assume clf is your trained classifier
prediction=clf.predict([[0, 2, 1, 0]]) # Double brackets for 2D input

print("prediction for input[0,2,1,0]:",prediction)
print(x_pred)