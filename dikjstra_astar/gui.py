import tkinter as tk
from algorithms import dijkstra, astar
import networkx as nx

# Coordinates for each city
coordinates = {
    "Poipet": (100, 103),
    "Oddar Meanchey": (190, 40),
    "Preah Vihear": (392, 70),
    "Ratanakiri": (660, 75),
    "Stueng Treng": (560, 120),
    "Banteay Meanchey": (143, 118),
    "Pailin": (80, 215),
    "Battambang": (170, 190),
    "Siem Reap": (265, 150),
    "Pursat": (260, 255),
    "Kampong Chhnang": (355, 330),
    "Kampong Thom": (390, 235),
    "Mondulkiri": (690, 260),
    "Koh Kong": (90, 360),
    "Kampong Cham": (480, 330),
    "Kratie": (585, 265),
    "Phnom Penh": (430, 390),
    "Kandal": (450, 420),
    "Kampong Speu": (325, 405),
    "Tboung Khmom": (570, 350),
    "Sihanoukville": (140, 460),
    "Kampot": (262, 470),
    "Kep": (273, 487),
    "Takeo": (390, 485),
    "Prey Veng": (520, 405),
    "Svay Rieng": (560, 465),
}

# Distances between cities
distances = {
    "Poipet,Oddar Meanchey": 85,
    "Poipet,Banteay Meanchey": 100,
    "Pailin,Battambang": 100,
    "Banteay Meanchey,Siem Reap": 100,
    "Oddar Meanchey,Preah Vihear": 100,
    "Oddar Meanchey,Banteay Meanchey": 100,
    "Preah Vihear,Siem Reap": 100,
    "Preah Vihear,Stueng Treng": 100,
    "Stueng Treng,Ratanakiri": 100,
    "Stueng Treng,Kratie": 100,
    "Stueng Treng,Kampong Thom": 100,
    "Banteay Meanchey,Battambang": 100,
    "Kampong Cham,Kratie": 100,
    "Kandal,Kampong Chhnang": 100,
    "Battambang,Siem Reap": 100,
    "Battambang,Pursat": 100,
    "Siem Reap,Kampong Thom": 100,
    "Pailin,Koh Kong": 100,
    "Koh Kong,Pursat": 100,
    "Koh Kong,Sihanoukville": 100,
    "Sihanoukville,Kampot": 100,
    "Pursat,Kampong Chhnang": 100,
    "Kampot,Kep": 100,
    "Kampong Chhnang,Kampong Speu": 100,
    "Kampong Chhnang,Kampong Thom": 100,
    "Kampong Chhnang,Kampong Cham": 100,
    "Kampong Cham,Kampong Thom": 100,
    "Mondulkiri,Ratanakiri": 100,
    "Mondulkiri,Kratie": 100,
    "Kratie,Tboung Khmom": 100,
    "Tboung Khmom,Prey Veng": 100,
    "Svay Rieng,Prey Veng": 100,
    "Prey Veng,Kandal": 100,
    "Kandal,Kampong Cham": 100,
    "Kampong Thom,Kratie": 100,
    "Takeo,Kandal": 100,
    "Takeo,Kep": 100,
    "Kandal,Phnom Penh": 100,
    "Kampong Speu,Kampot": 100,
    "Kampong Speu,Takeo": 100,
    "Kampong Cham,Tboung Khmom": 100,
    "Kampong Cham,Prey Veng": 100,
    "Pursat,Kampong Speu": 100,
}

# Create a graph
G = nx.Graph()

# Add nodes with coordinates
for location, (x, y) in coordinates.items():
    G.add_node(location, pos=(x, y))

# Add edges with distances
for edge, weight in distances.items():
    cities = edge.split(",")
    G.add_edge(cities[0], cities[1], weight=weight)

# Function to highlight the shortest path on the canvas
def highlight_shortest_path(path):
    for i in range(len(path) - 1):
        edge = (path[i], path[i + 1])
        (x1, y1) = coordinates[edge[0]]
        (x2, y2) = coordinates[edge[1]]
        canvas.create_line(x1, y1, x2, y2, fill="green", width=3, tags="highlighted_path")

# Function to handle button click event
def find_shortest_path():
    source = source_var.get()
    destination = destination_var.get()

    if source in coordinates and destination in coordinates:
        # Clear previous highlighted paths
        canvas.delete("highlighted_path")

        # Find the shortest path using Dijkstra's algorithm
        shortest_path = dijkstra(G, source, destination)

        # Highlight the shortest path on the canvas
        highlight_shortest_path(shortest_path)   

def find_path():
    algorithm = algorithm_var.get()
    source = source_var.get()
    destination = destination_var.get()

    if source in coordinates and destination in coordinates:
        # Clear previous highlighted paths
        canvas.delete("highlighted_path")

        # Find the path using the selected algorithm
        if algorithm == "Dijkstra":
            shortest_path = dijkstra(G, source, destination)
        elif algorithm == "A*":
            shortest_path = astar(G, source, destination)
        else:
            print("Invalid algorithm selected.")

        # Highlight the path on the canvas
        highlight_shortest_path(shortest_path) 

# Function to draw points and edges on the canvas
def draw_graph():
    # Draw edges
    for edge in G.edges():
        (x1, y1) = coordinates[edge[0]]
        (x2, y2) = coordinates[edge[1]]
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=1) 

        # Show distance text
        distance_text = f"{G[edge[0]][edge[1]]['weight']} km"
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2 + 10
        canvas.create_text(mid_x, mid_y, text=distance_text, font=("Arial", 7, "bold"), fill="red")

    # Draw nodes
    for location, (x, y) in coordinates.items():
        canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill="#e74c3c", outline="#c0392b", width=1)  # Red nodes with border
        canvas.create_text(x - 20, y,  text=location, anchor=tk.W, font=("Arial", 8, "bold"), fill="#2c3e50")  # Node labels

def clear_paths():
    # Clear previous highlighted paths
    canvas.delete("highlighted_path")

# Create a GUI
root = tk.Tk()
root.title("Cambodia Shortest Routes")

# Create a canvas to draw on
canvas = tk.Canvas(root, width=800, height=600, bg="#ecf0f1")  # Light gray background
canvas.pack()

# Entry widgets for source and destination cities with more space above and moved to the right
tk.Label(root, text="Source:").pack(side=tk.LEFT, pady=50, padx=10)
source_var = tk.StringVar()
source_entry = tk.Entry(root, textvariable=source_var)
source_entry.pack(side=tk.LEFT, pady=50, padx=10)

tk.Label(root, text="Destination:").pack(side=tk.LEFT, pady=50, padx=10)
destination_var = tk.StringVar()
destination_entry = tk.Entry(root, textvariable=destination_var)
destination_entry.pack(side=tk.LEFT, pady=50, padx=10)

# Dropdown menu for algorithm selection
tk.Label(root, text="Select Algorithm:").pack(side=tk.LEFT, pady=50, padx=10)
algorithm_var = tk.StringVar()
algorithm_var.set("Dijkstra")  # Default algorithm
algorithm_menu = tk.OptionMenu(root, algorithm_var, "Dijkstra", "A*")
algorithm_menu.pack(side=tk.LEFT, pady=50, padx=10)

# Button to find the shortest path with more space above and moved to the right
find_button = tk.Button(root, text="Find Shortest Path", command=find_path)
find_button.pack(side=tk.LEFT, pady=50, padx=10)
clear_button = tk.Button(root, text="Clear Paths", command=clear_paths)
clear_button.pack(side=tk.LEFT, pady=50, padx=10)

# Draw the graph on the canvas
draw_graph()

# Run the GUI
root.mainloop()