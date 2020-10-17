import numpy as np

class Graph:
    def __init__(self, nx_graph):
        self.num_nodes = 0
        self.weights = np.zeros((self.num_nodes, self.num_nodes), dtype='int')
        self.nx_graph = nx_graph

    def read_file(self, path):
        file = open(path, "r")

        self.num_nodes = int(file.readline().strip())
        self.weights = np.zeros((self.num_nodes, self.num_nodes), dtype='int')

        for v in range(self.num_nodes):
            self.nx_graph.add_node(v)

        for line in file:
            segments = line.split(' ')
            i1 = int(segments[0].strip())
            i2 = int(segments[1].strip())
            w = int(segments[2].strip())

            self.weights[i1][i2] = w
            self.weights[i2][i1] = w

            self.nx_graph.add_edge(i1, i2, weight=w)

    def calc_tree_weight(self, tree):
        sum = 0
        for (v, w) in tree:
            sum = sum + self.weights[v][w]

        return sum
