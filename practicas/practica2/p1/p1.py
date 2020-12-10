# 1) TSP
import sys
import numpy as np
from Graph import Graph

if __name__ == '__main__':

# Start with a graph

    graph = Graph(sys.argv[1])

# Find MST

    graph.findMST()

# Find minimum cost perfect matching

# Add these edges to tree and find eulerian tour

# Take shortcuts
