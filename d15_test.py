from unittest import TestCase

import aoc
from d15 import p1, p2


class D15_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d15_data()
        self.example_data = '''Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'''

    # Part 1 Tests
    def test_p1_examples(self):
        self.assertEqual(p1(self.example_data), 62842880)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data), 13882464)

    # Part 2 Tests
    def test_p2_examples(self):
        self.assertEqual(p2(self.example_data), 57600000)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data), 11171160)
