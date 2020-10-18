import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
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
        if neighbour in self.neighbours:
            pass
        self.neighbours.append(neighbour)

    def __str__(self):
        return str(self.id)

class Graph:
    def __init__(self, file, b):
        self.num_nodes = 0
        self.weights = np.zeros((self.num_nodes, self.num_nodes), dtype='int')
        self.nx_graph = nx.Graph()
        self.nodes = []
        self.weight_range = [1, 100]
        self.width_range = [0.2, 2.5]
        self.tree = None
        self.b = b

        self.read_file(file)

    def set_tree(self, tree):
        self.tree = tree

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

    def calc_tree_weight(self):
        sum = 0
        for (v, w) in pairwise(self.tree):
            sum = sum + self.weights[v.id][w.id]

        return sum

    def get_tree_edges(self):
        edges = []
        for (u, v) in pairwise(self.tree):
            edges.append((u.id, v.id))

        return edges

    def get_tree_labels(self, tree_edges):
        tree_labels = {}
        for (u, v) in tree_edges:
            tree_labels[(u, v)] = self.weights[u][v]
        return tree_labels

    def get_tree_line_widths(self, tree_edges):
        widths = []
        for (i, j) in tree_edges:
            widths.append(np.interp(self.weights[(i, j)], self.weight_range, self.width_range))
        return widths

    def get_graph_labels(self):
        labels = {}
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                dist = self.weights[i][j]
                if dist != 0 and not ((j, i) in labels):
                    labels[(i, j)] = dist
        return labels

    def get_graph_line_widths(self):
        widths = []
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                widths.append(np.interp(self.weights[(i, j)], self.weight_range, self.width_range))
        return widths

    def draw(self):
        positions = nx.shell_layout(self.nx_graph)

        graph_labels = self.get_graph_labels()
        graph_widths = self.get_graph_line_widths()

        tree_edges = self.get_tree_edges()
        tree_labels = self.get_tree_labels(tree_edges)
        tree_widths = self.get_tree_line_widths(tree_edges)
        tree_weight = self.calc_tree_weight()
        if tree_weight <= self.b:
            result = "Se encontró el árbol buscado"
        else:
            result = "No se encontró el árbol buscado"

        plt.tight_layout()
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()

        plt.subplot(1, 2, 1)
        plt.axis("off")
        plt.title("Peso esperado: {}".format(self.b))
        nx.draw_networkx(self.nx_graph, positions, edge_color='black',width=1,linewidths=1, node_size=1000,node_color='pink',alpha=0.9)
        nx.draw_networkx_edges(self.nx_graph, positions, tree_edges, arrows=True, width=graph_widths)
        nx.draw_networkx_edge_labels(self.nx_graph, positions, edge_labels=graph_labels, font_color='red', alpha=0.7)

        plt.subplot(1, 2, 2)
        plt.axis("off")
        plt.title("Peso del árbol generado: {}\n{}".format(tree_weight, result))
        nx.draw_networkx_nodes(self.nx_graph, positions, node_size=1000, node_color='pink', alpha=0.4)
        nx.draw_networkx_labels(self.nx_graph, positions)
        nx.draw_networkx_edges(self.nx_graph, positions, tree_edges, arrows=True, width=tree_widths)
        nx.draw_networkx_edge_labels(self.nx_graph,positions, edge_labels=tree_labels, font_color='red', alpha=0.7)

        plt.show()
