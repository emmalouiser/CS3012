import sys
sys.dont_write_bytecode = True

from DAG import Graph
import unittest
from sys import stdout
from coverage import Coverage

cov = Coverage()
cov.set_option('report:show_missing', True)
cov.start()

def LCA(graph, a, b):
    if a in graph.vertices() and b in graph.vertices():
        dfs_a = graph.dfs_recursive(a, [])
        dfs_b = graph.dfs_recursive(b, [])

        for i in range(min(len(dfs_a), len(dfs_b))):
          if dfs_a[i] == dfs_b[i]:
              return dfs_a[i]
        else:
            return -1;

    else:
        return -1;

class TestStringMethods(unittest.TestCase):

    def test_LCA_basic(self):
        g = {   1: [2, 3],
                2: [4, 5],
                3: [5],
                4: [6],
                5: [6],
                6: [7],
                7: []}

        graph = Graph(g)

        self.assertEqual(LCA(graph, 4, 5), 6)
        self.assertEqual(LCA(graph, 43, 35), -1)

    def test_null(self):
        graph = Graph()
        self.assertEqual(LCA(graph, 4, 5), -1)

    def test_no_LCA(self):
        g = {   1: [2, 3],
                2: [4, 5],
                3: [5],
                4: [6],
                5: [6],
                6: [7],
                7: []}

        graph = Graph(g)

        self.assertEqual(LCA(graph, 1, 7), -1)

    def test_vertices_not_in_graph(self):
        g = {   1: [2, 3],
                2: [4, 5],
                3: [5],
                4: [6],
                5: [6],
                6: [7],
                7: []}

        graph = Graph(g)

        self.assertEqual(LCA(graph, 43, 35), -1)

unittest.main(exit=False)

cov.stop()
cov.report()
