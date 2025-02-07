import networkx as nx
from gui import coordinates

def dijkstra(graph, start, end):
    # Initialize distances and predecessors
    distances = {node: float('infinity') for node in graph.nodes()}
    predecessors = {node: None for node in graph.nodes()}
    distances[start] = 0

    # Priority queue to keep track of nodes to visit
    priority_queue = list(graph.nodes())

    while priority_queue:
        current_node = min(priority_queue, key=lambda node: distances[node])
        priority_queue.remove(current_node)

        for neighbor in graph.neighbors(current_node):
            new_distance = distances[current_node] + graph[current_node][neighbor]['weight']
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node

    # Reconstruct the path from end to start
    path = []
    current_node = end
    while current_node is not None:
        path.insert(0, current_node)
        current_node = predecessors[current_node]

    return path


# A* search algorithm
def heuristic(node, goal):
    # Simple Euclidean distance as the heuristic
    (x1, y1) = coordinates[node]
    (x2, y2) = coordinates[goal]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def astar(graph, start, goal):
    # Initialize costs and predecessors
    costs = {node: float('infinity') for node in graph.nodes()}
    predecessors = {node: None for node in graph.nodes()}
    costs[start] = 0

    # Priority queue to keep track of nodes to visit
    priority_queue = list(graph.nodes())

    while priority_queue:
        current_node = min(priority_queue, key=lambda node: costs[node] + heuristic(node, goal))
        priority_queue.remove(current_node)

        for neighbor in graph.neighbors(current_node):
            new_cost = costs[current_node] + graph[current_node][neighbor]['weight']
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                predecessors[neighbor] = current_node

    # Reconstruct the path from goal to start
    path = []
    current_node = goal
    while current_node is not None:
        path.insert(0, current_node)
        current_node = predecessors[current_node]

    return path