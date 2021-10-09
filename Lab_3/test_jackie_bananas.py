import unittest
from jackie_bananas import jackie_bananas


class JackieTest(unittest.TestCase):
    def test_banana_1(self):
        test_jackie_bananas = jackie_bananas([3, 6, 7, 11], 8)

        right_jackie_bananas = 4

        self.assertEqual(test_jackie_bananas, right_jackie_bananas)

    def test_banana_2(self):
        test_jackie_bananas = jackie_bananas([30, 11, 23, 4, 20], 5)

        right_jackie_bananas = 30

        self.assertEqual(test_jackie_bananas, right_jackie_bananas)

    def test_banana_3(self):
        test_jackie_bananas = jackie_bananas([30, 11, 23, 4, 20], 4)

        right_jackie_bananas = -1

        self.assertEqual(test_jackie_bananas, right_jackie_bananas)
