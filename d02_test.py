from unittest import TestCase

import aoc
from d02 import p1, p2


class D02_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d02_data()

    # Part 1 Tests
    def test_p1_examples(self):
        self.assertEqual(p1('2x3x4'), 58)
        self.assertEqual(p1('1x1x10'), 43)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data), 1588178)

    # Part 2 Tests
    def test_p2_examples(self):
        self.assertEqual(p2('2x3x4'), 34)
        self.assertEqual(p2('1x1x10'), 14)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data), 3783758)
