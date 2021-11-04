import unittest
from bfs import bfs


class BFSTest(unittest.TestCase):

    def test_positive_result(self):
        graph = {
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

        self.assertEqual(bfs(graph, 'A'), list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']))

    def test_number_result(self):
        graph_numbers = {
            '0': ['1', '2'],
            '1': ['3', '4'],
            '2': ['5', '6'],
            '3': ['7', '8'],
            '4': [],
            '5': [],
            '6': [],
            '7': [],
            '8': []
        }

        self.assertEqual(bfs(graph_numbers, '0'), list(['0', '1', '2', '3', '4', '5', '6', '7', '8']))

    def test_wrong_result(self):
        wrong_graph = {
            'A': ['C', 'B'],
            'B': ['E', 'D'],
            'C': ['F', 'G'],
            'D': ['H', 'I'],
            'E': [],
            'F': [],
            'G': [],
            'H': [],
            'I': []
        }

        self.assertNotEqual(bfs(wrong_graph, 'A'), list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']))


if __name__ == '__main__':
    unittest.main()
