# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 06:23:15 2025

@author: jayes
"""

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

dataset=pd.read_csv("C:/Users/jayes/Downloads/Mall_Customers.csv")
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
dataset['Genre']=le.fit_transform(dataset['Genre'])
x=dataset.iloc[:,1:].values
cor=dataset.corr()
sns.heatmap(cor,square=True)
plt.title('Correlation Heatmap')
plt.show()

scaler=StandardScaler()
x_std=scaler.fit_transform(x)

clt=AgglomerativeClustering(linkage="complete",metric="euclidean",n_clusters=3)
model=clt.fit(x_std)

dataset["cluster"]=model.labels_
fig=plt.figure(); ax=fig.add_subplot(111)
scatter=ax.scatter(dataset['Age'],dataset['Annual Income (k$)'],c=dataset["cluster"],s=50)
ax.set_title("Agglomerative Clustering")
ax.set_xlabel("Age")
ax.set_ylabel("Annual Income (k$)")
plt.colorbar(scatter)
plt.show()
