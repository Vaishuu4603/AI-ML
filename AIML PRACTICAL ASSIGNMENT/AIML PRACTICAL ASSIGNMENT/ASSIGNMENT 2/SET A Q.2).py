# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 11:48:25 2025

@author: jayes
"""



visited=[]
queue=[]

def bfs(visited, graph, node):
    queue = []
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        
        for n in graph[m]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

# Define graph (same as before)
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = []  # List to keep track of visited nodes

print("Following in BFS:")
bfs(visited, graph, '5')





