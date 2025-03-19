from typing import List
class EdgeWeightedDigraph:
    def __init__(self, n_vertices : int):
        self.n_vertices = n_vertices
        self.edges_from_vertex : List[list] = []
        for _ in range(n_vertices):
            self.edges_from_vertex.append([])

    def add_edge(self, edge):
        self.edges_from_vertex[edge[0]].append(edge)

    def add_edges(self, source, edges):
        self.edges_from_vertex[source].extend(edges)

    def get_edges_from(self, vertex : int):
        return self.edges_from_vertex[vertex]

    def __repr__(self):
        s = ""
        for vertex in range(self.n_vertices):
            s += f"Vertex {vertex}: "
            for edge in self.edges_from_vertex[vertex]:
                s += f"{edge} "
            s += "\n"
        return s