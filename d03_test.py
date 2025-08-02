from unittest import TestCase

import aoc
from d03 import p1, p2


class D03_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d03data()

    # Part 1 Tests
    def test_p1_examples(self):
        self.assertEqual(p1('>'), 2)
        self.assertEqual(p1('^>v<'), 4)
        self.assertEqual(p1('^v^v^v^v^v'), 2)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data), 2572)

    # Part 2 Tests
    def test_p2_examples(self):
        self.assertEqual(p2('^v'), 3)
        self.assertEqual(p2('^>v<'), 3)
        self.assertEqual(p2('^v^v^v^v^v'), 11)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data), 2631)
