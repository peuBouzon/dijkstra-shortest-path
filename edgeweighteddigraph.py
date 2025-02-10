from bag import Bag

class EdgeWeightedDigraph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.n_edges = 0
        self.edges_from_vertex = Bag()
        for _ in n_vertices:
            self.edges_from_vertex.add(Bag())

    def add_edge(self, edge):
        self.edges_from_vertex[edge.source].add(edge)
        self.n_edges += 1

    def edges(self, vertex):
        return self.edges_from_vertex[vertex]