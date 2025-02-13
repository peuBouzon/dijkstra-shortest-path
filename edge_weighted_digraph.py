from linked_list import LinkedList
from directed_edge import DirectedEdge

class EdgeWeightedDigraph:
    def __init__(self, n_vertices : int):
        self.n_vertices = n_vertices
        self.n_edges = 0
        self.edges_from_vertex = []
        for _ in range(n_vertices):
            self.edges_from_vertex.append(LinkedList())

    def add_edge(self, edge : DirectedEdge):
        self.edges_from_vertex[edge.source].add(edge)
        self.n_edges += 1

    def get_edges_from(self, vertex : int):
        return self.edges_from_vertex[vertex]