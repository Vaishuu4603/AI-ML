# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 06:42:47 2025

@author: jayes
"""

import pyfpgrowth
import pandas as pd
data=pd.DataFrame({
    
    'MILK':[1,1,1,1,0],
    'BREAD':[1,1,0,1,1],
    'BUTTER':[1,0,0,1,1],
    'DIAPERS':[0,1,1,0,0],
    'BEER':[0,0,1,0,0]
    
 })

transaction = [row.index[row == 1].tolist() for _, row in data.iterrows()]

patterns=pyfpgrowth.find_frequent_patterns(transaction,2)

print(patterns)

