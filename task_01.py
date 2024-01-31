import networkx as nx
import matplotlib.pyplot as plt


topo_graph = nx.DiGraph(
    [
        ("f", "a"),
        ("a", "b"),
        ("a", "e"),
        ("b", "c"),
        ("b", "d"),
        ("d", "e"),
        ("f", "c"),
        ("f", "g"),
        ("h", "f"),
    ]
)

for layer, nodes in enumerate(nx.topological_generations(topo_graph)):
    for node in nodes:
        topo_graph.nodes[node]["layer"] = layer

# Graph rendering options
edge_line_style = "dashed"
options = {
    "with_labels": True,
    "font_size": 10,
    "font_weight": "bold",
    "node_size": 700,
    "font_color": "white",
    "node_color": "blueviolet",
    "width": 1.5,
    "style": edge_line_style,
}

if __name__ == "__main__":
    # Information about graph
    num_nodes = topo_graph.number_of_nodes()
    num_edges = topo_graph.number_of_edges()
    density = nx.density(topo_graph)
    print(
        "Graph information:",
        f"Number of nodes: {num_nodes}",
        f"Number of edges:{num_edges}",
        f"Density of the graph: {density:.5f}",
        sep="\n",
    )

    # Visualize the graph
    pos = nx.multipartite_layout(topo_graph, subset_key="layer")
    fig, ax = plt.subplots()
    nx.draw_networkx(topo_graph, pos=pos, ax=ax, **options)
    ax.set_title("Topograph")
    fig.tight_layout()
    plt.show()
