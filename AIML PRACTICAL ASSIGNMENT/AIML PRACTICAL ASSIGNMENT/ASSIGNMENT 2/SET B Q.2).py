# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 11:55:08 2025

@author: jayes
"""

def dls(graph,start, goal,dl,path):
    if dl<0:
       return None
    if start==goal:
        return path+[start]
    
    for n in graph.get(start,[]):
        if n not in path:
            result=dls(graph,n,goal,dl-1,path+[start])
            
            if result:
                return result
    return None

graph={
       
       'A':set(['B','C']),
       'B':set(['A','D','E']),
       'C':set(['A','F']),
       'D':set(['B']),
       'E':set(['B']),
       'F':set(['C'])
       
       
       }

result=dls(graph,'A','F',2,[])
if result:
    print("Goal Found:",result)
else:
    print("Goal not found within depth limit")















