import math
from directed_edge import DirectedEdge
from edge_weighted_digraph import EdgeWeightedDigraph
from priorityqueue import MinIndexPriorityQueue

class DijkstraShortestPath:
    def __init__(self, graph : EdgeWeightedDigraph, source : int) -> None:
        self.source = source
        self.distances = [math.inf] * graph.n_vertices
        self.distances[source] = 0
        self.edge_to = [None] * graph.n_vertices
        self.priority_queue = MinIndexPriorityQueue(max_size=graph.n_vertices)

        self.priority_queue.insert(source, 0.0)
        while self.priority_queue:
            self.relax(graph, self.priority_queue.pop()[0])

    def get_source(self):
        return self.source

    def get_distances(self):
        return self.distances

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


if __name__ == '__main__':
    source = 0
    graph = EdgeWeightedDigraph(5)
    graph.add_edge(DirectedEdge(0, 1, 1.0))
    graph.add_edge(DirectedEdge(0, 2, 8.4))
    graph.add_edge(DirectedEdge(1, 2, 8.2))
    graph.add_edge(DirectedEdge(1, 3, 6.1))
    graph.add_edge(DirectedEdge(2, 3, 9.0))
    graph.add_edge(DirectedEdge(3, 4, 32.0))
    dijkstra = DijkstraShortestPath(graph, source)

    for vertex in range(5):
        if vertex == source:
            print(f'Source vertex: {source}')
            continue

        path = dijkstra.get_path_to(vertex)
        vertices_in_path = []
        while True:
            try:
                e = path.pop()
                vertices_in_path.append(str(e.target))
            except IndexError:
                break
            
        print(f'Path to vertex {vertex}: {source} -> {' -> '.join(vertices_in_path)} ({dijkstra.get_distance_to(vertex)})')