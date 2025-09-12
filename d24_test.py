from unittest import TestCase

import aoc
from d24 import p1, p2


class D24_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d24_data()
        self.test_data = '''1
2
3
4
5
7
8
9
10
11'''

    # Part 1 Tests
    def test_p1_examples(self):
        self.assertEqual(p1(self.test_data), 99)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data), 10723906903)

    # Part 2 Tests
    def test_p2_examples(self):
        self.assertEqual(p2(self.test_data), 44)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data), 74850409)
