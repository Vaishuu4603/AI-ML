# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 11:40:29 2025

@author: jayes
"""

def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()
    
    visited.add(start)
    print(start,end=" ")
    
    for n in graph[start]:
        if n not in visited:
            dfs(graph,n,visited)
            
    return visited

graph={
       
       '5':['3','7'],
       '3':['2','4'],
       '7':['8'],
       '2':[],
       '4':['8'],
       '8':[]
       
       
       
       }
dfs(graph, '5')






