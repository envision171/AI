# Kruskal's Algorithm in Python

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.edges = []  # List to store all edges

    # Function to add an edge to the graph
    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    # Find function using union-find with path compression
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Union function with union by rank
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    # Function to perform Kruskal's algorithm
    def kruskal_mst(self):
        # Sort all edges by ascending weight
        self.edges = sorted(self.edges, key=lambda item: item[2])
        
        parent = []
        rank = []
        
        # Initialize the parent and rank arrays
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        
        mst = []  # Resultant MST list

        # Go through the sorted edges and pick the smallest edge, if it doesn't form a cycle
        for u, v, w in self.edges:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)
            
            # If including this edge doesn't cause a cycle, include it in the MST
            if root_u != root_v:
                mst.append([u, v, w])
                self.union(parent, rank, root_u, root_v)
        
        # Print the MST
        print("Edges in the Minimum Spanning Tree:")
        for u, v, w in mst:
            print(f"{u} -- {v} == {w}")

# Example usage:
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal_mst()
