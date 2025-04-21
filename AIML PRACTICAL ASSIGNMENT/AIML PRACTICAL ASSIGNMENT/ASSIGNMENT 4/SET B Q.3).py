# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 07:45:45 2025

@author: jayes
"""

import pandas as pd
import numpy as np
from scipy import stats

# Load dataset
df = pd.read_csv("C:/Users/jayes/Downloads/Mall_Customers.csv")

# Select numerical columns
numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()

# Compute z-scores
z_scores = np.abs(stats.zscore(df[numerical_cols]))

# Set threshold
threshold = 3

# Find outliers
outliers = (z_scores > threshold)
outliers_indices = np.where(outliers)
outliers_data = df.iloc[outliers_indices[0]]

# Print results
print("Outlier detected:")
print(outliers_data)
