# This code is part of an assignment of my master's degree.

from dijkstra import Dijkstra
from edgeweighteddigraph import EdgeWeightedDigraph
from directededge import DirectedEdge
from typing import Tuple

def get_graph_and_source_from_txt(path : str) -> Tuple[EdgeWeightedDigraph, int]:
    with open(path, 'r') as file:
        lines = file.readlines()
        dijkstra_source_vertex = int(lines[0].strip().replace('node_', ''))
        n_vertices = len(lines[1].strip().split(','))
        graph = EdgeWeightedDigraph(n_vertices)
        for line in lines[1:]:
            entries = line.strip().split(',')
            source = int(entries[0].replace('node_', ''))
            for target, weight in enumerate(entries[1:]):
                try:
                    weight = float(weight)
                    if weight > 0:
                        graph.add_edge(DirectedEdge(source, target + 1, weight))
                except ValueError:
                    # Ignore edges with non numeric weights
                    pass

        return graph, dijkstra_source_vertex


graph, source = get_graph_and_source_from_txt('input.txt')

dijkstra = Dijkstra(graph, source)
dijkstra.distances
print(dijkstra.distances)