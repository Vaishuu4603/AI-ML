# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 06:57:46 2025

@author: jayes
"""

import pandas as pd
from scipy import stats
data=pd.read_csv("C:/Users/jayes/Downloads/diabetes.csv")
mean=data['Glucose'].mean()
median=data['Glucose'].median
mode_result=stats.mode(data['Glucose'],keepdims=True)

print(f"Mean:{mean},Median:{median},Mode:{mode_result.mode[0]}")
