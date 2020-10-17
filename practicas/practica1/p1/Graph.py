import numpy as np
from itertools import tee

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def get_node(nodes, id):
    for node in nodes:
        if node.id == id:
            return node

class Node:

    def __init__(self, id):
        self.id = id
        self.neighbours = []
        self.visited = False

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

class Graph:
    def __init__(self, nx_graph):
        self.num_nodes = 0
        self.weights = np.zeros((self.num_nodes, self.num_nodes), dtype='int')
        self.nx_graph = nx_graph
        self.nodes = []

    def read_file(self, path):
        file = open(path, "r")

        self.num_nodes = int(file.readline().strip())
        self.weights = np.zeros((self.num_nodes, self.num_nodes), dtype='int')

        for v in range(self.num_nodes):
            self.nx_graph.add_node(v)
            self.nodes.append(Node(v))

        for line in file:
            segments = line.split(' ')
            i1 = int(segments[0].strip())
            i2 = int(segments[1].strip())
            w = int(segments[2].strip())

            self.weights[i1][i2] = w
            self.weights[i2][i1] = w

            self.nx_graph.add_edge(i1, i2, weight=w)
            for node in self.nodes:
                if node.id == i1:
                    node.add_neighbour(get_node(self.nodes, i2))
                if node.id == i2:
                    node.add_neighbour(get_node(self.nodes, i1))

    def calc_tree_weight(self, tree):
        sum = 0
        for (v, w) in pairwise(tree):
            sum = sum + self.weights[v.id][w.id]

        return sum

    def get_tree_edges(self, tree):
        edges = []
        for (u, v) in pairwise(tree):
            edges.append((u.id, v.id))

        return edges
