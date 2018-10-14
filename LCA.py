from DAG import Graph

def LCA( graph, a, b):
    dfs_a = graph.dfs_recursive(a, [])
    dfs_b = graph.dfs_recursive(b, [])

    for i in range(len(dfs_a)):
      if dfs_a[i] == dfs_b[i]:
          return dfs_a[i]
    else:
        return -1;

g = {   1: [2, 3],
        2: [4, 5],
        3: [5],
        4: [6],
        5: [6],
        6: [7],
        7: []}

graph = Graph(g)

print(LCA(graph, 4, 5))
