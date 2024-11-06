# Function to implement Prim's Algorithm without using a heap
def prim(graph, start):
    n = len(graph)
    mst = []  # Store MST edges
    visited = [False] * n
    visited[start] = True

    # Repeat until all vertices are in MST
    while len(mst) < n - 1:
        min_edge = None
        for u in range(n):
            if visited[u]:
                for v in range(n):
                    if not visited[v] and graph[u][v] != 0:
                        if min_edge is None or graph[u][v] < min_edge[0]:
                            min_edge = (graph[u][v], u, v)

        # Add the minimum edge to MST
        weight, u, v = min_edge
        visited[v] = True
        mst.append((u, v, weight))

    return mst

# Function to print the MST
def print_mst(mst):
    print("Edge   Weight")
    for u, v, weight in mst:
        print(f"{u} - {v}    {weight}")

# Example graph as adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# Start Prim's algorithm from vertex 0
mst = prim(graph, 0)

# Output the MST
print_mst(mst)
