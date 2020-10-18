import sys
import numpy as np
import random

if __name__ == '__main__':
    num_nodes = int(sys.argv[1])
    edge_prob = int(sys.argv[2])

    print(num_nodes)

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            print(i, j, np.random.randint(100) + 1)
