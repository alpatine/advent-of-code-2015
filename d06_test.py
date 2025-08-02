from unittest import TestCase

import aoc
from d06 import p1, p2


class D06_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d06data()

    # Part 1 Tests
    def test_p1_examples(self):
        self.assertEqual(p1('turn on 0,0 through 999,999'), 1000000)
        self.assertEqual(p1('toggle 0,0 through 999,0'), 1000)
        self.assertEqual(p1('turn off 499,499 through 500,500'), 0)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data), 543903)

    # Part 2 Tests
    def test_p2_examples(self):
        self.assertEqual(p2('turn on 0,0 through 0,0'), 1)
        self.assertEqual(p2('toggle 0,0 through 999,999'), 2000000)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data), 14687245)
