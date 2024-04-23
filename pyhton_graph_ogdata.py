import json
import networkx as nx
import matplotlib.pyplot as plt

# Load JSON data
with open('/content/data.json') as f:
    data = json.load(f)

# Create a graph
G = nx.Graph()

# Add routers as nodes
for entry in data['isis-database-information']:
    for db_entry in entry['isis-database']:
        for neighbor in db_entry.get('isis-database-entry', []):
            lsp_id = neighbor['lsp-id'][0]['data']
            G.add_node(lsp_id)

# Add connections between routers as edges
for entry in data['isis-database-information']:
    for db_entry in entry['isis-database']:
        for neighbor in db_entry.get('isis-database-entry', []):
            lsp_id = neighbor['lsp-id'][0]['data']
            neighbors = neighbor.get('isis-neighbor', [])
            for n in neighbors:
                neighbor_id = n['is-neighbor-id'][0]['data']
                G.add_edge(lsp_id, neighbor_id)

# Draw the graph with spacious layout
pos = nx.spring_layout(G, k=10.0)  # Adjust the value of k to make the layout more spacious

# Draw nodes and edges
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='skyblue', alpha=0.7)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

# Add labels
nx.draw_networkx_labels(G, pos, font_size=8)

# Enable interactive mode for zooming
plt.title('ISIS Network Visualization')
plt.axis('on')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(False)
plt.tight_layout()
plt.margins(0.1)
plt.axis('off')  # Hide axes for better visualization
plt.show()
