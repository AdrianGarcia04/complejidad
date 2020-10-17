import sys
import numpy as np

if __name__ == '__main__':
    num_nodes = int(sys.argv[1])
    edge_prob = int(sys.argv[2])

    print(num_nodes)
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            coin = int(np.random.rand() * 1000 % 100)
            if edge_prob >= coin:
                print(i, j, np.random.randint(100) + 1)
            else:
                pass
