# -*- coding: utf-8 -*-
"""
Write a python program to implement Data Normalization/Standardization - Rescale values 
of columns using Standardscaler() or minmaxScaler() for a given dataset. [use any dataset]
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Sample dataset (replace this with pd.read_csv() for real data)
data = {
    'Age': [18, 22, 25, 45, 35],
    'Salary': [20000, 25000, 32000, 60000, 52000]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# ---------------- MinMaxScaler (Normalization) ----------------
minmax_scaler = MinMaxScaler()
normalized_data = minmax_scaler.fit_transform(df)

df_normalized = pd.DataFrame(normalized_data, columns=df.columns)
print("\nAfter Min-Max Normalization:\n", df_normalized)

# ---------------- StandardScaler (Standardization) ----------------
standard_scaler = StandardScaler()
standardized_data = standard_scaler.fit_transform(df)

df_standardized = pd.DataFrame(standardized_data, columns=df.columns)
print("\nAfter Standardization:\n", df_standardized)
