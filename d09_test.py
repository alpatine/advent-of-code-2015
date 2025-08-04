from unittest import TestCase

import aoc
from d09 import p1, p2


class D09_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d09data()

    # Part 1 Tests
    def test_p1_examples(self):
        data = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""
        self.assertEqual(p1(data), 605)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data), 117)

    # Part 2 Tests
    def test_p2_examples(self):
        data = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""
        self.assertEqual(p2(data), 982)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data), 909)

