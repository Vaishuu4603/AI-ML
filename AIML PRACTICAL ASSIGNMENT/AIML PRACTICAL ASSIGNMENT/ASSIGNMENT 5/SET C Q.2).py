# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 19:41:45 2025

@author: jayes
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("C:/Users/jayes/Downloads/Admission_Predict.csv")

# Check the first few rows
print(df.head())

# Rename column for convenience
df.rename(columns={"Chance of Admit ": "Chance_of_Admit"}, inplace=True)

# Convert to binary classification: Admission Status (0/1) based on threshold
df['Admission_Status'] = (df['Chance_of_Admit'] >= 0.75).astype(int)

# Drop non-useful columns
if 'Serial No.' in df.columns:
    df.drop(['Serial No.'], axis=1, inplace=True)
df.drop(['Chance_of_Admit'], axis=1, inplace=True)

# Independent features (X) and target (y)
X = df.drop('Admission_Status', axis=1)
y = df['Admission_Status']

# Feature Scaling (optional but helpful)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into training and testing (80/20)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# -------- Model 1: Logistic Regression --------
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred_logreg = logreg.predict(X_test)

# -------- Model 2: Random Forest --------
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# -------- Evaluation --------
print("=== Logistic Regression ===")
print("Accuracy:", accuracy_score(y_test, y_pred_logreg))
print(classification_report(y_test, y_pred_logreg))

print("\n=== Random Forest Classifier ===")
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred_rf)
sns.heatmap(cm, annot=True, fmt='d', cmap='Purples', xticklabels=["No", "Yes"], yticklabels=["No", "Yes"])
plt.title("Confusion Matrix - Random Forest")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
