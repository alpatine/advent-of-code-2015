from unittest import TestCase

import aoc
from d20 import p1, p2


class D20_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d20_data()

    # Part 1 Tests
    def test_p1_examples(self):
        self.assertEqual(p1('10'), 1)
        self.assertEqual(p1('20'), 2)
        self.assertEqual(p1('30'), 2)
        self.assertEqual(p1('40'), 3)
        self.assertEqual(p1('50'), 4)
        self.assertEqual(p1('60'), 4)
        self.assertEqual(p1('70'), 4)
        self.assertEqual(p1('80'), 6)
        self.assertEqual(p1('90'), 6)
        self.assertEqual(p1('100'), 6)
        self.assertEqual(p1('110'), 6)
        self.assertEqual(p1('120'), 6)
        self.assertEqual(p1('130'), 8)
        self.assertEqual(p1('140'), 8)
        self.assertEqual(p1('150'), 8)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data), 786240)

    # Part 2 Tests
    # def test_p2_examples(self):
    #     data = ''''''
    #     self.assertEqual(p2(data), 0)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data), 831600)
