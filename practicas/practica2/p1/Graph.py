import math
import numpy as np
from itertools import tee
from collections import deque

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.neighbors = []

    def add_neighbor(self, n):
        self.neighbors.append(n)

    def remove_neighbor(self, n):
        self.neighbors.remove(n)

    def clean(self):
        self.neighbors = []

    def __str__(self):
        return str(f'{self.id}: {self.x},{self.y}')

class Edge:
    def __init__(self, v1, v2, d):
        self.v1 = v1
        self.v2 = v2
        self.d = d

    def __str__(self):
        return str(f'({self.v1}) {self.d} ({self.v2})')

class Graph:
    def __init__(self, file, create_edges=True):
        self.nodes = []
        self.edges = []
        self.file = file
        self.read_file(file)
        if create_edges:
            self.create_edges()

    def read_file(self, path):
        file = open(path, "r")
        lines = list(filter(lambda a: len(a) > 0, file.read().split('\n')))

        vertex_set = list(filter(lambda a: a[0].isdigit(), lines))
        cities = list(map(lambda x: tuple(x.split(' ')[1:]), vertex_set))
        self.nodes = [Node(i, int(c[0]), int(c[1])) for i, c in enumerate(cities)]

    def add_edge(self, edge):
        self.edges.append(edge)

    def remove_edge(self, edge):
        self.edges.remove(edge)

    def create_edges(self):
        self.edges = []
        for i, u in enumerate(self.nodes):
            for j, v in enumerate(self.nodes[i + 1:]):
                d = math.sqrt((int(v.x - u.x) ** 2) + (int(v.y - u.y) ** 2))
                self.edges.append(Edge(u.id, v.id, d))

                u.neighbors.append(v)
                v.neighbors.append(u)

    def conex(self):
        visited = []
        for edge in self.edges:
            visited.append(edge.v1)
            visited.append(edge.v2)
        return len(self.nodes) == len(list(set(visited)))

    def cycle(self):
        visited = [False for i in self.nodes]
        for i in self.nodes:
            if not visited[self.nodes.index(i)] and self.cycleaux(self.nodes.index(i), visited):
                return True
        return False

    def cycleaux(self, s, visited):
        parent = [-1 for i in self.nodes]
        q = deque()
        visited[s] = True
        q.append(s)
        while q:
            u = q.pop()
            for v in self.nodes[u].neighbors:
                if not visited[self.nodes.index(v)]:
                    visited[self.nodes.index(v)] = True
                    q.append(self.nodes.index(v))
                    parent[self.nodes.index(v)] = u
                elif parent[u] != self.nodes.index(v):
                    return True
        return False

    def findMST(self):
        sorted_edges = sorted(self.edges, key = lambda edge: edge.d)

        tree = Graph(self.file, create_edges=False)

        # while not tree.conex():
        #     for edge in sorted_edges:
        #         tree.add_edge(edge)
        #         if tree.cycle():
        #             tree.remove_edge(edge)

        while not tree.conex():
            tree.add_edge(sorted_edges.pop(0))
            if tree.cycle():
                tree.remove_edge(edge)

        for e in tree.edges:
            print(e)
        self.spaning_tree = tree
