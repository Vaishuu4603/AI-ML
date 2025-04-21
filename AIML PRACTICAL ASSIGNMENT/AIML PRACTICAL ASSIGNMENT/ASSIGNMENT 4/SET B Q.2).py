# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 07:38:08 2025

@author: jayes
"""

import numpy as np
from scipy import stats

Group_a=[85,78,90,88,76]
Group_b=[82,79,75,90,84]

T_Statistic,p_value=stats.ttest_ind(Group_a,Group_b)

print("T-Statistics:",T_Statistic)
print("P-value:",p_value)

Alpha=0.05
if p_value<Alpha:
    print("Reject the null hypothesis:There is a significance difference between  the test scores")
else:
    print("fail to reject the null hypothesis : No significant different in test scores")
    