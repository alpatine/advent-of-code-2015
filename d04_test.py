from unittest import TestCase

import aoc
from d04 import p1, p2


class D04_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d04data()

    # Part 1 Tests
    def test_p1_examples(self):
        self.assertEqual(p1('abcdef'), 609043)
        self.assertEqual(p1('pqrstuv'), 1048970)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data), 117946)

    # Part 2 Tests
    # def test_p2_examples(self):
    #     self.assertEqual(p2(''), 0)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data), 3938038)
