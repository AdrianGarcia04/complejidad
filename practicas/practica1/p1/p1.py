# b) Árbol Generador con pesos: Dada una gráfica no
# dirigida y conexa G = (V, E), con pesos en las aristas
# y un entero positivo B, ¿existe un árbol generador
# para G con peso menor o igual que B?

import sys
import numpy as np
from itertools import tee
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
    graph = Graph()
    graph.read_file(file)

    # Creating random tree
    num_nodes = graph.num_nodes
    nodes = list(np.random.choice(num_nodes, size=num_nodes, replace=False))
    tree = []
    for v, w in pairwise(nodes):
        tree.append((v, w))

    # Checking if the tree weighs less than b
    tree_weight = graph.calc_tree_weight(tree)
    print(tree_weight < b)
