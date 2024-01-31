import networkx as nx

from task_01 import topo_graph

weights = {
    ("f", "a"): 1,
    ("a", "b"): 4,
    ("a", "e"): 2,
    ("b", "c"): 6,
    ("b", "d"): 9,
    ("d", "e"): 10,
    ("f", "c"): 6,
    ("f", "g"): 8,
    ("h", "f"): 2,
}

nx.set_edge_attributes(topo_graph, weights, "weight")


def dijkstra(graph, start):
    dst = {n: float("inf") for n in graph.nodes()}
    dst[start] = 0

    visited = {n: False for n in graph.nodes()}

    while False in visited.values():
        cur_node = min(
            [node for node in graph.nodes() if visited[node] is False],
            key=lambda node: dst[node],
        )
        visited[cur_node] = True

        for neighbour, weight in graph[cur_node].items():
            if dst[cur_node] + weight["weight"] < dst[neighbour]:
                dst[neighbour] = dst[cur_node] + weight["weight"]

    return dst


if __name__ == "__main__":
    print(dijkstra(topo_graph, "h"))
