# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 07:57:59 2025

@author: jayes
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data={
      'A':[1,2,3,4,5],
      'B':[2,3,4,5,6],
      'C':[5,4,3,2,1],
      'D':[3,4,2,4,3]
      
      
      }
df=pd.DataFrame(data)
corr_matrix=df.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm',fmt=".2F",square=True,linewidths=0.5)

plt.title('coreelation Matrix Heatmap')
plt.show()