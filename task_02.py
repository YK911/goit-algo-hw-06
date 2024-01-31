from task_01 import topo_graph
from helpers import dfs, bfs

if __name__ == "__main__":
    print("Result from DFS algorithm")
    dfs(topo_graph, "h")
    print("\n")
    print("Result from BFS algorithm")
    bfs(topo_graph, "h")
