import math
import unittest
from dijkstra_shortest_path import DijkstraShortestPath
from edge_weighted_digraph import EdgeWeightedDigraph

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.graph = EdgeWeightedDigraph(6)
        self.graph.add_edge((0, 1, 1.0))
        self.graph.add_edge((0, 2, 4.0))
        self.graph.add_edge((1, 2, 2.0))
        self.graph.add_edge((1, 3, 6.0))
        self.graph.add_edge((2, 3, 3.0))
        self.graph.add_edge((3, 4, 1.0))
        self.dijkstra = DijkstraShortestPath(self.graph, 0)

    def test_has_path_to(self):
        for i in range(1,5):
            self.assertTrue(self.dijkstra.has_path_to(i))
        self.assertFalse(self.dijkstra.has_path_to(5))

    def test_shortest_path(self):
        for i, distance in enumerate([0.0, 1.0, 3.0, 6.0, 7.0, math.inf]):
            self.assertEqual(distance, self.dijkstra.get_distance_to(i))

if __name__ == '__main__':
    unittest.main()