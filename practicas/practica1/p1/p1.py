# b) Árbol Generador con pesos: Dada una gráfica no
# dirigida y conexa G = (V, E), con pesos en las aristas
# y un entero positivo B, ¿existe un árbol generador
# para G con peso menor o igual que B?

import sys
import numpy as np
import random
from Graph import Graph

if __name__ == '__main__':
    # Reading args
    file = sys.argv[1]
    b = int(sys.argv[2])

    # Reading file
    graph = Graph(file, b)

    # Creating a random tree
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

    # Set tree in the graph
    graph.set_tree(tree)

    # Draw all
    graph.draw()
