from dijkstra_shortest_path import DijkstraShortestPath
import graph_factory
import output_handler

if __name__ == '__main__':
    import time
    import argparse
    import timeit
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    args = parser.parse_args()

    start = time.time()
    graph, source = graph_factory.from_txt(args.input)
    time_to_build = time.time() - start
    print(f'Time to build the graph: {time_to_build:f}')

    times = timeit.Timer(lambda : DijkstraShortestPath(graph, source)).repeat(repeat=3000, number=1)
    time_dijkstra = min(times)
    print(f'Time to find shortest paths:: {time_dijkstra:f}')
    print(f'total: {time_to_build + time_dijkstra:f}')

    shortest_paths = DijkstraShortestPath(graph, source)

    output_handler.to_txt(shortest_paths, args.output)