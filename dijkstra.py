import math
from directededge import DirectedEdge
from edgeweighteddigraph import EdgeWeightedDigraph

class Dijkstra:
    def __init__(self, edge_weighted_digraph : EdgeWeightedDigraph, source : int) -> None:
        self.graph = edge_weighted_digraph
        self.source = source
        self.distances = [math.inf] * edge_weighted_digraph.n_vertices
        self.distances[source] = 0
        self.edge_to = [None] * edge_weighted_digraph.n_vertices

    def get_distance_to(self, vertex : int):
        pass

    def has_path_to(vertex : int):
        pass

    def get_path_to(vertex : int):
        pass

    def _relax(self, edge : DirectedEdge):
        if self.get_distance_to(edge.target) > self.get_distance_to(edge.source)  + edge.weight:
            self.distances[edge.target] = self.get_distance_to(edge.source)  + edge.weight
            self.edge_to[edge.target] = edge

    def relax(self, graph : EdgeWeightedDigraph, vertex : int):
        for edge in graph.get_edges_from(vertex):
            self._relax(edge)

