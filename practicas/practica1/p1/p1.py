# b) Árbol Generador con pesos: Dada una gráfica no
# dirigida y conexa G = (V, E), con pesos en las aristas
# y un entero positivo B, ¿existe un árbol generador
# para G con peso menor o igual que B?

import sys
import numpy as np
import networkx as nx
from itertools import tee
import matplotlib.pyplot as plt
from Graph import Graph

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

if __name__ == '__main__':
    # Reading args
    file = sys.argv[1]
    b = int(sys.argv[2])

    # Reading file
    graph = Graph(nx.Graph())
    graph.read_file(file)

    # Creating random tree
    num_nodes = graph.num_nodes
    nodes = list(np.random.choice(num_nodes, size=num_nodes, replace=False))
    tree = []
    for v, w in pairwise(nodes):
        tree.append((v, w))

    labels = {}
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            dist = graph.weights[i][j]
            if dist != 0 and not ((w, v) in labels):
                labels[(i, j)] = dist

    # Checking if the tree weighs less than b
    tree_weight = graph.calc_tree_weight(tree)
    print(tree_weight < b)

    options = {
        'node_color': 'pink',
        'node_size': 500,
        'width': 3,
    }

    positions = nx.shell_layout(graph.nx_graph)

    nx.draw_networkx(graph.nx_graph, positions, edge_color='black',width=1,linewidths=1, node_size=1000,node_color='pink',alpha=0.9)
    nx.draw_networkx_edge_labels(graph.nx_graph,positions, edge_labels=labels, font_color='red', alpha=0.7)

    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()

    plt.axis("off")
    plt.show()
