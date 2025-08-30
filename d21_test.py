from unittest import TestCase

import aoc
from d21 import p1, p2


class D21_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d21_data()

    # Part 1 Tests
    # def test_p1_examples(self):
    #     self.assertEqual(p1(''), 0)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data), 111)

    # Part 2 Tests
    # def test_p2_examples(self):
    #     self.assertEqual(p2(''), 0)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data), 188)
