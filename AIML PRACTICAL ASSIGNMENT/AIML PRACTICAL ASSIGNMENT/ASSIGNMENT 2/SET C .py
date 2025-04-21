from collections import deque

def bfs_path(graph, start, goal):
    queue = deque([[start]])
    visited = set([start])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                new_path = list(path)
                new_path.append(n)
                queue.append(new_path)
                
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'A'],
    'C': ['A', 'D'],
    'D': ['E', 'F'],
    'E': ['G', 'D'],
    'F': ['G', 'H'],
    'G': ['E', 'F']
}

start_node = 'A'
goal_node = 'G'
path = bfs_path(graph, start_node, goal_node)

if path:
    print(f"Path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path from {start_node} to {goal_node}")
