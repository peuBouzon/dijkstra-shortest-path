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
    print(f'Time to build the graph: {time.time() - start}')

    #elapsed = timeit.timeit(lambda : DijkstraShortestPath(graph, source), number=10)
    #print(f'timeit: {elapsed / 10}')
    start = time.time()

    shortest_paths = DijkstraShortestPath(graph, source)
    print(f'Time to find shortest paths: {time.time() - start}')

    output_handler.to_txt(shortest_paths, args.output)