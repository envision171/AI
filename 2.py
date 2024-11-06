import heapq


class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start node
        self.h = 0  # Heuristic cost to goal node
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f


def heuristic(a, b):
    # Using Manhattan distance for the heuristic
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    open_list = []
    closed_list = set()

    start_node = Node(start)
    goal_node = Node(goal)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        # Generate neighbors (8 directions)
        neighbors = [
            (0, 1), (1, 0), (0, -1), (-1, 0),  # Horizontal and vertical
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonal
        ]

        for move in neighbors:
            neighbor_pos = (current_node.position[0] + move[0], current_node.position[1] + move[1])

            # Check if neighbor is within grid bounds and not an obstacle
            if (0 <= neighbor_pos[0] < len(grid) and
                    0 <= neighbor_pos[1] < len(grid[0]) and
                    grid[neighbor_pos[0]][neighbor_pos[1]] != 1):

                if neighbor_pos in closed_list:
                    continue

                g = current_node.g + 1  # Assume each move has a cost of 1
                h = heuristic(neighbor_pos, goal)
                neighbor_node = Node(neighbor_pos, current_node)
                neighbor_node.g = g
                neighbor_node.h = h
                neighbor_node.f = g + h

                if any(node.position == neighbor_pos and node.f <= neighbor_node.f for node in open_list):
                    continue

                heapq.heappush(open_list, neighbor_node)

    return None  # Path not found


grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)
path = astar(grid, start, goal)
print("Path found:", path)
