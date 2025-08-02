from unittest import TestCase

import aoc
from d05 import p1, p2


class D05_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d05data()

    # Part 1 Tests
    def test_p1_examples(self):
        self.assertEqual(p1('ugknbfddgicrmopn'), 1)
        self.assertEqual(p1('aaa'), 1)
        self.assertEqual(p1('jchzalrnumimnmhp'), 0)
        self.assertEqual(p1('haegwjzuvuyypxyu'), 0)
        self.assertEqual(p1('dvszwmarrgswjxmb'), 0)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data), 258)

    # Part 2 Tests
    def test_p2_examples(self):
        self.assertEqual(p2('qjhvhtzxzqqjkmpb'), 1)
        self.assertEqual(p2('xxyxx'), 1)
        self.assertEqual(p2('uurcxstgmygtbstg'), 0)
        self.assertEqual(p2('ieodomkazucvgmuy'), 0)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data), 53)
