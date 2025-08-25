from unittest import TestCase

import aoc
from d17 import p1, p2


class D17_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d17_data()
        self.example_data = '''20
15
10
5
5'''

    # Part 1 Tests
    def test_p1_examples(self):
        self.assertEqual(p1(self.example_data, 25), 4)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data, 150), 1638)

    # Part 2 Tests
    def test_p2_examples(self):
        self.assertEqual(p2(self.example_data, 25), 3)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data, 150), 17)
