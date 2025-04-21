# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 05:32:25 2025

@author: jayes
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv("C:/Users/jayes/Downloads/Mall_Customers.csv")
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
dataset['Genre']=le.fit_transform(dataset['Genre'])
x=dataset.iloc[:,1:].values

from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan, strategy="most_frequent")
imputer=imputer.fit(x)
x=imputer.transform(x)

from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x=sc_x.fit_transform(x)

from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=8,init='k-means++',max_iter=300,n_init=10,random_state=0)
y_kmeans=kmeans.fit_predict(x)
dataset['Cluster']=y_kmeans
print(dataset.head())