# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 21:48:13 2025

@author: jayes
"""

import pandas as pd

"""
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

df=pd.read_csv("C:/Users/jayes/Downloads/BostonHousing.csv")

x=df.iloc[:,:-1]
y=df.iloc[:,-1]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
knn=KNeighborsRegressor(n_neighbors=5)
knn.fit(x_train,y_train)

predictions=knn.predict(x_test)
mse=mean_squared_error(y_test,predictions)
print("Mean Squared Error:",mse)
"""

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
boston = load_boston()
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2, random_state=42)

# Train KNN Regressor
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train, y_train)

# Make predictions
predictions = knn.predict(X_test)

# Evaluate performance using R² score (since it's regression)
r2 = r2_score(y_test, predictions)
print("R² Score:", r2)

















