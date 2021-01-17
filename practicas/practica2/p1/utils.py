import math
from Graph import *

def read(path):
	with open(path, 'r') as arch:
		l = list(filter(lambda x: len(x) > 0, arch.read().split('\n')))
		nodes = list(filter(lambda x: x[0].isdigit(), l))
		cities = list(map(lambda x: tuple(x.split(' ')[1:]), nodes))
		nodes = [Node(f"N_{i + 1}") for i, _ in enumerate(cities)]

		visit = []
		edges = []
		aux = 1

		for i, c1 in enumerate(cities):
			visit.append(c1)
			for j, c2 in enumerate(list(filter(lambda x: not x in visit, cities))):
				edges.append(Edge(nodes[i], nodes[j + aux], math.sqrt((int(c2[0]) - int(c1[0]))**2 + (int(c2[1]) - int(c1[1]))**2)))
			aux += 1
		return nodes, edges
