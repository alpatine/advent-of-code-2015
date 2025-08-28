from unittest import TestCase

import aoc
from d19 import p1, p2


class D19_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d19_data()

    # Part 1 Tests
    def test_p1_examples(self):
        data = '''H => HO
H => OH
O => HH

HOH'''
        self.assertEqual(p1(data), 4)
        data = '''H => HO
H => OH
O => HH

HOHOHO'''
        self.assertEqual(p1(data), 7)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data), 576)

    # Part 2 Tests
    # def test_p2_examples(self):
    #     data = ''''''
    #     self.assertEqual(p2(data), 6)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data), 207)
