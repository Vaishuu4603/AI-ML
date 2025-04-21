# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch

df=pd.read_csv("C:/Mall_Customers.csv")
x=df.iloc[:,[3,4]].values
dendrogram = sch.dendrogram(sch.linkage(x,method='single'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distance')
plt.show()

hc=AgglomerativeClustering(n_clusters=5,linkage='single')
y_hc=hc.fit_predict(x)

plt.scatter(x[y_hc == 0,0], x[y_hc == 0,1],s=100,c='red', label='cluster1')
plt.scatter(x[y_hc == 1,0], x[y_hc == 1,1],s=100,c='blue', label='cluster2')
plt.scatter(x[y_hc == 2,0], x[y_hc == 2,1],s=100,c='green', label='cluster3')
plt.scatter(x[y_hc == 3,0], x[y_hc == 3,1],s=100,c='cyan', label='cluster4')
plt.scatter(x[y_hc == 4,0], x[y_hc == 4,1],s=100,c='pink', label='cluster5')

plt.title('cluster of customer')
plt.xlabel('Annual Income(k$)')
plt.ylabel('Spending Score(1-100)')
plt.legend()
plt.show()