# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 05:50:59 2025

@author: jayes
"""

import pandas as pd
from apyori import apriori
df=pd.read_csv("C:/Users/jayes/Downloads/groceries - groceries.csv")
transaction=[]
for index,row in df.iterrows():
    transaction=[]
    for col in df.columns:
        if row[col]==1:
            transaction.append(col)
    transaction.append(transaction)
    
frequent_itemsets=apriori(transaction,min_support=0.5,min_confidence=0.7,min_lift=1.2,min_length=2)

rules=list(frequent_itemsets)
print("Frequent Itemsets and Association Rules:")
for rule in rules:
    print(rule)