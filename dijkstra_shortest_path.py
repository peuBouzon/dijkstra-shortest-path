import math
from edge_weighted_digraph import EdgeWeightedDigraph
from priorityqueue import MinIndexPriorityQueue

class DijkstraShortestPath:
    def __init__(self, graph : EdgeWeightedDigraph, source : int) -> None:
        self.source = source
        self.distances = [math.inf] * graph.get_n_vertices()
        self.distances[source] = 0
        self.edge_to = [None] * graph.get_n_vertices()
        self.priority_queue = MinIndexPriorityQueue(max_size=graph.get_n_vertices())

        self.priority_queue.insert(source, 0.0)
        while self.priority_queue:
            index_min, _ = self.priority_queue.pop()
            self.relax(graph, index_min)

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
        edge : tuple = self.edge_to[vertex]
        while edge is not None:
            path.append(edge)
            edge = self.edge_to[edge[0]]
        return path
    
    # tests whether the distance to the target vertex can be reduced by going through the edge
    # edge is composed by (source, target, weight)
    def _relax(self, edge : tuple):
        if self.distances[edge[1]] > self.distances[edge[0]] + edge[2]:
            self.distances[edge[1]] = self.distances[edge[0]] + edge[2]
            self.edge_to[edge[1]] = edge
            if (self.priority_queue.contains(edge[1])): # edge[1] is the target vertex
                self.priority_queue.change(edge[1], self.distances[edge[1]])
            else:
                self.priority_queue.insert(edge[1], self.distances[edge[1]])

    def relax(self, graph : EdgeWeightedDigraph, vertex : int):
        for edge in graph.get_edges_from(vertex):
            self._relax(edge)


if __name__ == '__main__':
    source = 0
    graph = EdgeWeightedDigraph(5)
    graph.add_edge((0, 1, 1.0))
    graph.add_edge((0, 2, 8.4))
    graph.add_edge((1, 2, 8.2))
    graph.add_edge((1, 3, 6.1))
    graph.add_edge((2, 3, 9.0))
    graph.add_edge((3, 4, 32.0))
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
                vertices_in_path.append(str(e[1]))
            except IndexError:
                break
            
        print(f'Path to vertex {vertex}: {source} -> {' -> '.join(vertices_in_path)} ({dijkstra.get_distance_to(vertex)})')