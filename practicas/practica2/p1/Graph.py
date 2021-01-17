import random
from collections import deque

class Node():
	def __init__(self, id):
		self.id = id
		self.vecinos = []
	def addNeigh(self, n):
		self.vecinos.append(n)
	def remNeigh(self, n):
		self.vecinos.remove(n)
	def __str__(self):
		return str(self.id)

class Edge():
	def __init__(self, v1, v2, d):
		self.v1 = v1
		self.v2 = v2
		self.d = d
	def graph(self):
		return (f"{self.v1}", f"{self.v2}")
	def __str__(self):
		return f"{str(self.v1)}, {str(self.v2)}: {str(self.s)}"

class Graph():

	def __init__(self, nodes = [], edges = []):
		self.nodes = nodes
		self.edges = edges
		for edge in self.edges:
			edge.v1.addNeigh(edge.v2)
			edge.v2.addNeigh(edge.v1)
		self.tree = self
		self.tour = []

	def addEdge(self, edge):
		for vertex in self.nodes:
			if vertex.id == edge.v1.id:
				vertex.addNeigh(edge.v2)
			elif vertex.id == edge.v2.id:
				vertex.addNeigh(edge.v1)
		self.edges.append(edge)

	def remEdge(self, edge):
		for vertex in self.nodes:
			if vertex.id == edge.v1.id:
				vertex.remNeigh(edge.v2)
			elif vertex.id == edge.v2.id:
				vertex.remNeigh(edge.v1)
		self.edges.remove(edge)

	def cycle2(self, s, visited):
		parent = [-1 for i in self.nodes]
		q = deque()
		visited[s] = True
		q.append(s)

		while q:
			u = q.pop()
			for v in self.nodes[u].vecinos:
				i = self.nodes.index(v)
				if not visited[i]:
					visited[i] = True
					q.append(i)
					parent[i] = u
				elif parent[u] != i:
					return True
		return False

	def has_cycle(self):
		visited = [False for i in self.nodes]
		for i in self.nodes:
			if not visited[self.nodes.index(i)] and self.cycle2(self.nodes.index(i), visited):
				return True
		return False

	def getTour(self, original_edges, original_nodes):
		pila = deque()
		s = random.choice(self.nodes)
		pila.append(s)
		visit = []

		while pila:
			top = pila.pop()
			visit.append(top)
			adj = top.vecinos
			for vertex in adj:
				if not vertex in visit:
					pila.append(vertex)

		visit.append(s)
		tour = []
		count = []
		for i, vertex in enumerate(visit):
			if i != len(visit) - 1:
				for edge in original_edges:
					if edge.v1.id == vertex.id and edge.v2.id == visit[i+1].id:
						tour.append(edge)
						if not edge.v1 in count:
							count.append(edge.v1)
						if not edge.v2 in count:
							count.append(edge.v2)

					elif edge.v2.id == vertex.id and edge.v1.id == visit[i+1].id:
						tour.append(edge)
						if not edge.v1 in count:
							count.append(edge.v1)
						if not edge.v2 in count:
							count.append(edge.v2)

		tourS = []
		tourS.append(tour[0])
		for edge in tour:
			if edge != tourS[len(tourS) - 1]:
				tourS.append(edge)
		tour = tourS[:]
		self.tour = tourS

	def conex(self):
		visit = []
		for edge in self.edges:
			visit.append(edge.v1)
			visit.append(edge.v2)
		return len(list(set(visit))) == len(self.nodes)

	def getTree(self):
		arInOrder = []
		nodes = []
		count = []
		for vertex in self.nodes:
			nodes.append(Node(vertex.id))

		for i, edge in enumerate(self.edges):
			for v1 in nodes:
				if edge.v1.id == v1.id:
					for v2 in nodes:
						if edge.v2.id == v2.id:
							if not (v1,v2) in count:
								arInOrder.append(Edge(v1, v2, edge.d))
								count.append((v1,v2))

				elif edge.v2.id == v1.id:
					for v2 in nodes:
						if edge.v1.id == v2.id:
							if not (v2,v1) in count:
								arInOrder.append(Edge(v2, v1, edge.d))
								count.append((v2,v1))

		arInOrder = sorted(arInOrder, key = lambda edge: edge.d)
		tree = Graph(nodes = nodes)
		while not tree.conex():
			for edge in arInOrder:
				tree.addEdge(edge)
				if tree.has_cycle():
					tree.remEdge(edge)
		self.tree = tree
