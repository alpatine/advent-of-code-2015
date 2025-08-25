from unittest import TestCase

import aoc
from d18 import p1, p2


class D18_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d18_data()

    # Part 1 Tests
    def test_p1_examples(self):
        data = '''.#.#.#
...##.
#....#
..#...
#.#..#
####..'''
        self.assertEqual(p1(data, 4), 4)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data, 100), 821)

    # Part 2 Tests
    def test_p2_examples(self):
        data = '''##.#.#
...##.
#....#
..#...
#.#..#
####.#
'''
        self.assertEqual(p2(data, 5), 17)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data, 100), 886)
