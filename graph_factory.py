from typing import Tuple
from directed_edge import DirectedEdge
from edge_weighted_digraph import EdgeWeightedDigraph

def from_txt(path : str) -> Tuple[EdgeWeightedDigraph, int]:
    dijkstra_source_vertex = None
    n_vertices = None
    graph = None
    with open(path, 'r') as file:
        for line in file:
            if not dijkstra_source_vertex:
                dijkstra_source_vertex = int(line.strip().replace('node_', ''))
                continue
            
            entries = line.strip().split(',')

            if not graph:
                n_vertices = len(entries)
                graph = EdgeWeightedDigraph(n_vertices)
        
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


