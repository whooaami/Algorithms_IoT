import unittest
from bfs import graph


class TestGraph(unittest.TestCase):

    def test_graph(self):
        expected_graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F', 'G'],
            'D': ['H', 'I'],
            'E': [],
            'F': [],
            'G': [],
            'H': [],
            'I': []
        }

        self.assertEqual(expected_graph, graph)


if __name__ == '__main__':
    unittest.main()
