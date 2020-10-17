# b) Árbol Generador con pesos: Dada una gráfica no
# dirigida y conexa G = (V, E), con pesos en las aristas
# y un entero positivo B, ¿existe un árbol generador
# para G con peso menor o igual que B?

import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
from Graph import Graph

if __name__ == '__main__':
    # Reading args
    file = sys.argv[1]
    b = int(sys.argv[2])

    # Reading file
    graph = Graph(nx.Graph())
    graph.read_file(file)

    stack = [np.random.choice(graph.nodes)]
    tree = []
    while stack:
        v = stack.pop()
        if not v.visited:
            v.visited = True
            tree.append(v)
            random.shuffle(v.neighbours)
            for w in v.neighbours:
                stack.append(w)

    labels = {}
    for i in range(graph.num_nodes):
        for j in range(i + 1, graph.num_nodes):
            dist = graph.weights[i][j]
            if dist != 0 and not ((j, i) in labels):
                labels[(i, j)] = dist


    # Checking if the tree weighs less than b
    tree_weight = graph.calc_tree_weight(tree)
    tree_edges = graph.get_tree_edges(tree)
    tree_labels = {}
    for (u, v) in tree_edges:
        tree_labels[(u, v)] = graph.weights[u][v]
    print(tree_weight)

    positions = nx.shell_layout(graph.nx_graph)

    plt.tight_layout()
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()

    plt.subplot(1, 2, 1)
    nx.draw_networkx(graph.nx_graph, positions, edge_color='black',width=1,linewidths=1, node_size=1000,node_color='pink',alpha=0.9)
    nx.draw_networkx_edge_labels(graph.nx_graph,positions, edge_labels=labels, font_color='red', alpha=0.7)

    plt.subplot(1, 2, 2)
    nx.draw_networkx_nodes(graph.nx_graph, positions, node_size=1000,node_color='pink',alpha=0.4)
    nx.draw_networkx_labels(graph.nx_graph, positions)
    nx.draw_networkx_edges(graph.nx_graph, positions, tree_edges, arrows=True)
    nx.draw_networkx_edge_labels(graph.nx_graph,positions, edge_labels=tree_labels, font_color='red', alpha=0.7)
    # nx.draw_networkx_edge_labels(graph.nx_graph,positions, edge_labels=labels, font_color='red', alpha=0.7)

    plt.axis("off")
    plt.show()
