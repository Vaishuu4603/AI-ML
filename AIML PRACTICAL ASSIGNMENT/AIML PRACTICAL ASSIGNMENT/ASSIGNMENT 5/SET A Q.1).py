# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 19:16:56 2025

@author: jayes
"""

import numpy as np
from sklearn.linear_model import LinearRegression
x=np.array([1,2,3,4,5,6,7,8]).reshape((-1,1))
print(x)
y=np.array([7,14,15,18,19,21,26,23]).reshape((-1,1))
print(y)
model=LinearRegression()
model.fit(x,y)
x_new=np.array(9).reshape((-1,1))
y_new_pred=model.predict(x_new)
print(y_new_pred)
print('Slope:-',model.coef_)
