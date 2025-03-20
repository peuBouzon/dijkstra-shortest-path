from dijkstra_shortest_path import DijkstraShortestPath
import time
# write the distance and shortest path to each vertex to a txt file
def to_txt(dijkstra : DijkstraShortestPath, output_file : str):
    source = dijkstra.get_source()
    start = time.time()
    vertices_ordered_by_distance = [i[0] for i in sorted(enumerate(dijkstra.get_distances()), key=lambda x: x[1])]
    print(f'Time to sort vertices: {time.time() - start:f}')
    output = [f'SHORTEST PATH TO node_{source}: node_{source} <- node_{source} (Distance: 0.00)']
    for vertex in vertices_ordered_by_distance:
        if vertex == source:
            continue
        else:
            path = dijkstra.get_path_to(vertex)
            if not path:
                continue
            else:
                reversed_path = [f'node_{path[0][1]}']
                for edge in path:
                    reversed_path.append(f'node_{edge[0]}')
                str_path = ' <- '.join(reversed_path)
                output.append(f'SHORTEST PATH TO node_{vertex}: {str_path} (Distance: {dijkstra.get_distance_to(vertex):.2f})')

    with open(output_file, 'w') as f:
        f.write('\n'.join(output))