import numpy as np
import matplotlib.pyplot as plt; plt.ion()
import networkx as nx

def find_lowest_common_ancestor(graph, a, b):
    """
    Find the lowest common ancestor in the directed, acyclic graph of node a and b.
    The LCA is defined as on

    @reference:
    https://en.wikipedia.org/wiki/Lowest_common_ancestor

    Notes:
    ------
    This definition is the opposite of the term as it is used e.g. in biology!

    Arguments:
    ----------
        graph: networkx.DiGraph instance
            directed, acyclic, graph

        a, b:
            node IDs

    Returns:
    --------
        lca: [node 1, ..., node n]
            list of lowest common ancestor nodes (can be more than one)
    """

    assert nx.is_directed_acyclic_graph(graph), "Graph has to be acyclic and directed."

    # get ancestors of both (intersection)
    common_ancestors = list(nx.descendants(graph, a) & nx.descendants(graph, b))

    # get sum of path lengths
    sum_of_path_lengths = np.zeros((len(common_ancestors)))
    for ii, c in enumerate(common_ancestors):
        sum_of_path_lengths[ii] = nx.shortest_path_length(graph, a, c) \
                                  + nx.shortest_path_length(graph, b, c)

    # print common_ancestors
    # print sum_of_path_lengths

    # return minima
    minima, = np.where(sum_of_path_lengths == np.min(sum_of_path_lengths))

    return [common_ancestors[ii] for ii in minima]

def test():

    nodes = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
    edges = [("a","b"),
             ("b","c"),
             ("b","d"),
             ("a","e"),
             ("a","h"),
             ("e","f"),
             ("e","g"),
             ("e","i"),
             ("h","l"),
             ("h","m"),
             ("g","j"),
             ("o","p"),
             ("o","n"),
             ("n","m"),
             ("n","l"),
             ("n","k"),
             ("p","j"),]

    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    # plot
    pos = nx.spring_layout(G)
    nx.draw(G, pos)
    nx.draw_networkx_labels(G, pos, labels=dict([(c, c) for c in 'abcdefghijklmnop']))
    plt.show()

    a,b = 'a','o'
    lca = find_lowest_common_ancestor(G, a, b)
    print ("Lowest common ancestor(s) for {} and {}: {}".format(a, b, lca))

    return

if __name__ == "__main__":
    test()
