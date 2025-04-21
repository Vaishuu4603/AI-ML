# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 21:38:25 2025

@author: jayes
"""
# FOR LOAD WINE DATASET
"""
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

wine=load_wine()
x_train,x_test,y_train,y_test=train_test_split(wine.data,wine.target,test_size=0.2,random_state=42)

knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)

predictions=knn.predict(x_test)
accuracy=accuracy_score(y_test,predictions)
print("Accuracy:",accuracy)
"""

#FOR IRIS DATASET

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris=load_iris()
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.2,random_state=42)

knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)

predictions=knn.predict(x_test)
accuracy=accuracy_score(y_test,predictions)
print("Accuracy:",accuracy)