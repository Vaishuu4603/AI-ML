# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 10:00:04 2025

@author: jayes
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Load dataset
df = pd.read_csv("C:/Users/jayes/Downloads/breast-cancer (1).csv")

# Clean up column names (to fix hidden tab characters, spaces, etc.)
df.columns = df.columns.str.strip()

# Select features and target
x = df.iloc[:, [2, 3]].values  # These must be numeric columns
y = df.iloc[:, 4].values       # Target column (make sure this is numeric too)

# Split data
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=20)

# Encode categorical columns (AFTER fixing column names)
le = LabelEncoder()
df['mefalsepause'] = le.fit_transform(df['mefalsepause'])
df['falsede-caps'] = le.fit_transform(df['falsede-caps'])
df['breast'] = le.fit_transform(df['breast'])
df['breast-quad'] = le.fit_transform(df['breast-quad'])
df['irradiat'] = le.fit_transform(df['irradiat'])
df['class'] = le.fit_transform(df['class'])

# Train SVM
classifier = SVC(kernel='linear', random_state=0)
classifier.fit(X_train, y_train)

# Predict new value
y_pred = classifier.predict([[20, 8400]])
print("Predicted class:", y_pred)














