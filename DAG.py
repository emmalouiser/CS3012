import unittest
from sys import stdout
from coverage import Coverage

cov = Coverage()
cov.set_option('report:show_missing', True)
cov.start()

import sys
sys.dont_write_bytecode = True

class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = dict({})
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def dfs_recursive(self, vertex, path):
        path += [vertex]

        for neighbor in self.__graph_dict[vertex]:
            if neighbor not in path:
                path = self.dfs_recursive(neighbor, path)

        return path

class TestStringMethods(unittest.TestCase):

    def test_constructor(self):
        graph = Graph()
        self.assertEqual(graph.vertices(), [])
        self.assertEqual(graph.edges(), [])

    def test_constructor_notnull(self):
        g = {   1: [2, 3],
                2: [4, 5],
                3: [5],
                4: [6],
                5: [6],
                6: [7],
                7: []}

        graph = Graph(g)
        self.assertEqual(graph.vertices(), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(graph.edges(), [{1, 2}, {1, 3}, {2, 4}, {2, 5}, {3, 5}, {4, 6}, {5, 6}, {6, 7}])

    def test_add_vertex(self):
        graph = Graph()
        graph.add_vertex(2)
        self.assertEqual(graph.vertices(), [2])

    def test_add_vertex(self):
        graph = Graph()
        graph.add_vertex(2)
        self.assertEqual(graph.vertices(), [2])

    def test_add_edge(self):
        g = {   1: [2, 3],
                2: [4, 5],
                3: [5],
                4: [6],
                5: [6],
                6: [7],
                7: []}

        graph = Graph(g)
        graph.add_edge({2, 3})
        self.assertEqual(graph.edges(), [{1, 2}, {1, 3}, {2, 4}, {2, 5}, {2, 3}, {3, 5}, {4, 6}, {5, 6}, {6, 7}])


unittest.main(exit=False)

cov.stop()
cov.report()
