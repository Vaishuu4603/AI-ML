# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 08:06:24 2025

@author: jayes
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
data=np.random.randn(1000)
plt.hist(data,bins=30,color='blue',edgecolor='black',alpha=0.7)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()