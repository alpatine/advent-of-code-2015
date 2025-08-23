from unittest import TestCase

import aoc
from d14 import p1, p2


class D14_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d14_data()

    # Part 1 Tests
    def test_p1_examples(self):
        data = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""
        self.assertEqual(p1(data, 1), 16)
        self.assertEqual(p1(data, 10), 160)
        self.assertEqual(p1(data, 11), 176)
        self.assertEqual(p1(data, 12), 176)
        self.assertEqual(p1(data, 1000), 1120)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data), 2660)

    # Part 2 Tests
    def test_p2_examples(self):
        data = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""
        self.assertEqual(p2(data, 1), 1)
        self.assertEqual(p2(data, 140), 139)
        self.assertEqual(p2(data, 1000), 689)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data), 1256)

