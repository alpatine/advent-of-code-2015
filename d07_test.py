from unittest import TestCase

import aoc
from d07 import p1, p2


class D07_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d07_data()

    # Part 1 Tests
    def test_p1_examples(self):
        data = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""
        self.assertEqual(p1(data, 'd'), 72)
        self.assertEqual(p1(data, 'e'), 507)
        self.assertEqual(p1(data, 'f'), 492)
        self.assertEqual(p1(data, 'g'), 114)
        self.assertEqual(p1(data, 'h'), 65412)
        self.assertEqual(p1(data, 'i'), 65079)
        self.assertEqual(p1(data, 'x'), 123)
        self.assertEqual(p1(data, 'y'), 456)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data), 16076)

    # Part 2 Tests
    # def test_p2_examples(self):
    #     self.assertEqual(p2(''), 0)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data), 2797)
