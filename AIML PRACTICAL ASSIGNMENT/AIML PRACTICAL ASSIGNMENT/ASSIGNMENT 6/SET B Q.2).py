# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 06:06:09 2025

@author: jayes
"""

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
df=pd.read_csv("C:/Users/jayes/Downloads/groceries - groceries.csv")
records=[]
for i in range(0,9834):
    records.append([str(df.values[i,4])])

rules=apriori(records,min_support=0.0022,min_confidence=0.20,min_lift=3,min_length=4)
results=list(rules)
results_list=[]
for i in range(0,len(results)):
    results_list.append('RULE : \t'+str(results[i][0])+'\n SUPPORT :\t'+str(results[i][1]))
print(len(results_list))
print(results_list[0])