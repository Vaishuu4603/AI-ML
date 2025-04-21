# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 07:09:41 2025

@author: jayes
"""
"""
#ONE WAY
import numpy as np
from scipy import stats

group1=[23,20,21,22,25]
group2=[30,28,27,29,31]
group3=[35,32,34,36,37]

f_statistics,p_value=stats.f_oneway(group1,group2,group3)

print("F-Statistics",f_statistics)
print("P-value",p_value)

alpha=0.05

if p_value<alpha:
    print("Reject the null hypothesis:at least one group mean is differentr")
else:
    print("fail to reject the null hypothesis no significant difference between group means")
    """
 
    # TWO WAY
    
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf


data={
      
      'Exercise':['yoga','yoga','yoga','yoga','yoga','yoga','Running',
                  'Running','Running','Running','Running','Running'],
      
      'Diet':['low-carb','low-carb','Low-carb','High-protein','High-pritein',
              'Heigh-protein','Low-carb','Low-carb','Low-carb','Heigh-protein',
             'High-protein','High-protein' ],
      
      'WeightLoss':[2.1,2.5,2.3,2.4,2.6,2.8,4.2,4.5,4.8,5.0,5.2,5.4]
      
      
      
      }
df=pd.DataFrame(data)
model = smf.ols('WeightLoss ~ C(Exercise) + C(Diet) + C(Exercise):C(Diet)', data=df).fit()

annova_table=sm.stats.anova_lm(model,type=2)
print(annova_table)
























