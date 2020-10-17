import sys
import numpy as np
import Graph
import random

if __name__ == '__main__':
    num_nodes = int(sys.argv[1])
    edge_prob = int(sys.argv[2])

    print(num_nodes)

    nodes = [Graph.Node(i) for i in range(num_nodes)]

    for (u, v) in Graph.pairwise(nodes):
        print(u.id, v.id, np.random.randint(100) + 1)
    print(nodes[0].id, nodes[-1].id, np.random.randint(100) + 1)

    for i in range(num_nodes):
        for j in range(i + 2, num_nodes):
            coin = int(np.random.rand() * 1000 % 100)
            if edge_prob >= coin:
                print(i, j, np.random.randint(100) + 1)
            else:
                pass
