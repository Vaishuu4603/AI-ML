# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 07:03:58 2025

@author: jayes
"""

import pandas as pd

data=pd.read_csv("C:/Users/jayes/Downloads/diabetes.csv")
variance=data['Glucose'].var()
std_dev=data['Glucose'].std()
data_range = data['Glucose'].max() - data['Glucose'].min()


print(f"Variance:{variance},Standard Deviation:{std_dev},Range:{data_range}")
