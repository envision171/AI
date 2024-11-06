from collections import deque


# Depth First Search (DFS) using recursion
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Breadth First Search (BFS) using a queue
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# User input for graph construction
graph = {}
num_edges = int(input("Enter number of edges: "))
for _ in range(num_edges):
    u, v = input("Enter edge (u v): ").split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

# Choosing traversal type
start_node = input("Enter starting node: ")
traversal_type = input("Enter traversal type (DFS/BFS): ").strip().upper()

print(f"{traversal_type} traversal:")
if traversal_type == "DFS":
    dfs(graph, start_node)
elif traversal_type == "BFS":
    bfs(graph, start_node)
else:
    print("Invalid traversal type. Choose either DFS or BFS.")
