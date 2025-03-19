from typing import Tuple
from edge_weighted_digraph import EdgeWeightedDigraph

# creates a graph from the input txt file
def from_txt(path : str) -> Tuple[EdgeWeightedDigraph, int]:
    dijkstra_source_vertex = None
    n_vertices = None
    graph = None
    with open(path, 'r') as file:
        for line in file:
            if dijkstra_source_vertex is None:
                # the first line contains the source vertex
                dijkstra_source_vertex = int(line.strip().replace('node_', ''))
                continue
            
            entries = line.strip().split(',')

            if not graph:
                n_vertices = len(entries)
                graph = EdgeWeightedDigraph(n_vertices)

            source = int(entries[0].replace('node_', ''))
            edges = []
            for target, weight in enumerate(entries[1:]):
                try:
                    weight = float(weight)
                    # Ignore edges with non positive weights 
                    if weight > 0:
                        edges.append((source, target if target < source else target + 1, weight))
                except ValueError:
                    # Ignore edges with non numeric weights
                    pass
            graph.add_edges(source, edges)

    return graph, dijkstra_source_vertex


