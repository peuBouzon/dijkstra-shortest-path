from dijkstra_shortest_path import DijkstraShortestPath

def to_txt(dijkstra : DijkstraShortestPath, output_file : str):
    source = dijkstra.get_source()
    vertices_ordered_by_distance = [i[0] for i in sorted(enumerate(dijkstra.get_distances()), key=lambda x: x[1])]
    output = [f'SHORTEST PATH TO node_{source}: node_{source} <- node_{source} (Distance: 0.00)']
    for vertex in vertices_ordered_by_distance:
        if vertex == source:
            continue
        else:
            path = dijkstra.get_path_to(vertex)
            if not path:
                continue
            else:
                reversed_path = [f'node_{path[0].target}']
                for edge in path:
                    reversed_path.append(f'node_{edge.source}')
                str_path = ' <- '.join(reversed_path)
                output.append(f'SHORTEST PATH TO node_{vertex}: {str_path} (Distance: {dijkstra.get_distance_to(vertex):.2f})')

    with open(output_file, 'w') as f:
        f.write('\n'.join(output))