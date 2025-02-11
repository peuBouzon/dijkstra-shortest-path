import math
import unittest
from dijkstra import Dijkstra
from edgeweighteddigraph import EdgeWeightedDigraph
from directededge import DirectedEdge

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.graph = EdgeWeightedDigraph(6)
        self.graph.add_edge(DirectedEdge(0, 1, 1.0))
        self.graph.add_edge(DirectedEdge(0, 2, 4.0))
        self.graph.add_edge(DirectedEdge(1, 2, 2.0))
        self.graph.add_edge(DirectedEdge(1, 3, 6.0))
        self.graph.add_edge(DirectedEdge(2, 3, 3.0))
        self.graph.add_edge(DirectedEdge(3, 4, 1.0))
        self.dijkstra = Dijkstra(self.graph, 0)

    def test_has_path_to(self):
        for i in range(1,5):
            self.assertTrue(self.dijkstra.has_path_to(i))
        self.assertFalse(self.dijkstra.has_path_to(5))

    def test_shortest_path(self):
        for i, distance in enumerate([0.0, 1.0, 3.0, 6.0, 7.0, math.inf]):
            self.assertEqual(distance, self.dijkstra.get_distance_to(i))

if __name__ == '__main__':
    unittest.main()