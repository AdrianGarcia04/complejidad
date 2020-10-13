import numpy as np

class Graph:
    def __init__(self):
        self.num_nodes = 0
        self.weights = np.zeros((self.num_nodes, self.num_nodes), dtype='int')

    def read_file(self, path):
        file = open(path, "r")

        self.num_nodes = int(file.readline().strip())
        self.weights = np.zeros((self.num_nodes, self.num_nodes), dtype='int')

        for line in file:
            segments = line.split(' ')
            i1 = int(segments[0].strip())
            i2 = int(segments[1].strip())
            weight = int(segments[2].strip())

            self.weights[i1][i2] = weight
            self.weights[i2][i1] = weight

    def calc_tree_weight(self, tree):
        sum = 0
        for (v, w) in tree:
            sum = sum + self.weights[v][w]

        return sum
