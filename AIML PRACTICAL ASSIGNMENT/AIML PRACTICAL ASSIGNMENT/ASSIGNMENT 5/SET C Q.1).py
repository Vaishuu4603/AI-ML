# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 09:49:31 2025

@author: jayes
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load dataset
cancer = load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.2, random_state=42)

# Create and train SVM classifier
classifier = SVC(kernel='linear', random_state=0)
classifier.fit(x_train, y_train)

# Make predictions
predictions = classifier.predict(x_test)

# Evaluate
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)








