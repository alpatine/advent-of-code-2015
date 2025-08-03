from unittest import TestCase

import aoc
from d08 import p1, p2


class D08_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d08data()

    # Part 1 Tests
    def test_p1_examples(self):

        self.assertEqual(p1('""'), 2)
        self.assertEqual(p1('"abc"'), 2)
        self.assertEqual(p1('"aaa\\"aaa"'), 3)
        self.assertEqual(p1('"\\x27"'), 5)
        
        data = '""\n' \
        '"abc"\n' \
        '"aaa\\"aaa"\n' \
        '"\\x27"'
        self.assertEqual(p1(data), 12)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data), 1342)

    # Part 2 Tests
    def test_p2_examples(self):
        self.assertEqual(p2('""'), 4)
        self.assertEqual(p2('"abc"'), 4)
        self.assertEqual(p2('"aaa\\"aaa"'), 6)
        self.assertEqual(p2('"\\x27"'), 5)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data), 2074)
