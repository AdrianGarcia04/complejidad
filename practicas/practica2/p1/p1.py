from Graph import *
from utils import read
import sys
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
	(nodes, edges) = read(sys.argv[1])
	graph = Graph(nodes=nodes, edges=edges)
	graph.getTree()
	tree = graph.tree
	impares = list(filter(lambda v: len(v.vecinos) % 2 != 0, tree.nodes))
	aristImpares = []

	for node in impares:
		for edge in graph.edges:
			if edge.v1.id == node.id or edge.v2.id == node.id:
				aristImpares.append(edge)

	match = []
	for node in impares:
		minimum_edge = aristImpares[0]
		for edge in aristImpares:
			if node.id == edge.v1.id or node.id == edge.v2.id:
				if edge.d <= minimum_edge.d:
					minimum_edge = edge
				aristImpares.remove(edge)
		match.append(minimum_edge)

	matchArbol = tree.edges[:]
	for edge in match:
		if not edge in matchArbol:
			matchArbol.append(edge)

	newnodes = []
	newedgs = []
	count = []
	for v in tree.nodes:
		newnodes.append(Node(v.id))

	for e in matchArbol:
		for v1 in newnodes:
			if e.v1.id == v1.id:
				for v2 in newnodes:
					if e.v2.id == v2.id:
						if not (v1,v2) in count:
							newedgs.append(Edge(v1,v2,e.d))
							count.append((v1,v2))
			elif e.v2.id == v1.id:
				for v2 in newnodes:
					if e.v1.id == v2.id:
						if not (v2,v1) in count:
							newedgs.append(Edge(v2,v1,e.d))
							count.append((v2,v1))

	D = Graph(nodes=newnodes, edges=newedgs)
	D.getTour(graph.edges, graph.nodes)

	G = nx.Graph()
	nnodes = list(map(lambda v: v.id, graph.nodes))
	G.add_nodes_from(nnodes)

	paths = list(map(lambda e: e.graph(), D.tour))
	x = list(map(lambda edge: edge.graph(), graph.edges))
	y = list(map(lambda edge: edge.d, graph.edges))

	peso = 0
	for edge, d in zip(x, y):
		if edge in paths:
			G.add_edge(*edge,d=("%d" % d))
			peso += d

	plt.title("Peso del tour: {}\n".format(peso))

	pos = nx.spring_layout(G)
	edges = G.edges()
	labels = nx.get_edge_attributes(G,'d')

	nx.draw_networkx(G, pos=pos,\
	with_labels=True, \
	width=1.0, \
	node_size=1000, \
	node_color='pink',\
	alpha=0.9)
	nx.draw_networkx_edge_labels(G, pos, labels)

	plt.show()
