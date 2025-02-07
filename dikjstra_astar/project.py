import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create a graph representing provinces and their distances
G = nx.Graph()

# Add provinces as vertices with coordinates
provinces = {
    'Phnom Penh': (11, 11),
    'Siem Reap': (8, 14),
    'Battambang': (5, 10),
    'Sihanoukville': (13, 6),
    # Add more provinces with their coordinates
}

# Add vertices to the graph
for province, coordinates in provinces.items():
    G.add_node(province, pos=coordinates)

# Add edges with distances
G.add_edge('Phnom Penh', 'Siem Reap', weight=300)
G.add_edge('Phnom Penh', 'Battambang', weight=200)
G.add_edge('Siem Reap', 'Battambang', weight=250)
G.add_edge('Phnom Penh', 'Sihanoukville', weight=400)
# Add more edges with distances

# GUI using Tkinter
class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cambodia Province Map")

        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.canvas = FigureCanvasTkAgg(self.plot_graph(), master=self.canvas_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def plot_graph(self):
        pos = nx.get_node_attributes(G, 'pos')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        return plt

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
