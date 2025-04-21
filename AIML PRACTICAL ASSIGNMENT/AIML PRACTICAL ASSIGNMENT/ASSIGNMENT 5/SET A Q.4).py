# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 19:58:05 2025

@author: jayes
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

x=np.array([2.5,5.1,3.2,8.5,3.5,1.5,9.2,5.5,8.3,
            2.7,7.7,5.9,4.5,3.3,1.1,8.9,2.5,1.9,6.1,7.4,2.7,
            4.8]).reshape((-1,1))

print(x)

y=np.array([21,47,27,75,30,20,88,60,81,
            25,85,62,41,42,17,95,30,24,67,69,30,54])

print(y)

model=LinearRegression()
model.fit(x,y)
x_new=np.array(9).reshape((-1,1))
y_new_pred=model.predict(x_new)
print(y_new_pred)
print('Slope',model.coef_)