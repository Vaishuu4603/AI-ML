# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 18:53:07 2025

@author: jayes
"""

import random
def ai_agent():
    actions=["move left","move right","stay still"]
    
    return random.choice(actions)
for _ in range(5):
    print("AI Agent decides to:",ai_agent())