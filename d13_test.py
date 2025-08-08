from unittest import TestCase

import aoc
from d13 import p1, p2


class D13_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d13data()

    # Part 1 Tests
    def test_p1_examples(self):
        data = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""
        self.assertEqual(p1(data), 330)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data), 733)

    # Part 2 Tests
    # def test_p2_examples(self):
    #     self.assertEqual(p2(''), 0)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data), 725)

