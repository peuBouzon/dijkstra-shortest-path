import math
from directededge import DirectedEdge
from edgeweighteddigraph import EdgeWeightedDigraph
from priorityqueue import MinIndexPriorityQueue

class Dijkstra:
    def __init__(self, graph : EdgeWeightedDigraph, source : int) -> None:
        self.source = source
        self.distances = [math.inf] * graph.n_vertices
        self.distances[source] = 0
        self.edge_to = [None] * graph.n_vertices
        self.priority_queue = MinIndexPriorityQueue(max_size=graph.n_vertices)

        self.priority_queue.insert(source, 0.0)
        while self.priority_queue:
            self.relax(graph, self.priority_queue.pop()[0])

    def get_distance_to(self, vertex : int):
        return self.distances[vertex]

    def has_path_to(self, vertex : int):
        return not math.isinf(self.distances[vertex])

    def get_path_to(self, vertex : int):
        if not self.has_path_to(vertex):
            return None
        path = []
        edge : DirectedEdge = self.edge_to[vertex]
        while edge is not None:
            path.append(edge)
            edge = self.edge_to[edge.source]
        return path
 
    def _relax(self, edge : DirectedEdge):
        if self.distances[edge.target] > self.distances[edge.source] + edge.weight:
            self.distances[edge.target] = self.distances[edge.source] + edge.weight
            self.edge_to[edge.target] = edge
            if (self.priority_queue.contains(edge.target)):
                self.priority_queue.change(edge.target, self.distances[edge.target])
            else:
                self.priority_queue.insert(edge.target, self.distances[edge.target])

    def relax(self, graph : EdgeWeightedDigraph, vertex : int):
        for edge in graph.get_edges_from(vertex):
            self._relax(edge)

