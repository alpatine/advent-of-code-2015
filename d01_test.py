from unittest import TestCase

import aoc
from d01 import p1, p2


class D01_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.d1data = aoc.d01data()

    # Part 1 Tests
    def test_p1_examples(self):
        self.assertEqual(p1('(())'), 0)
        self.assertEqual(p1('()()'), 0)
        self.assertEqual(p1('((('), 3)
        self.assertEqual(p1('(()(()('), 3)
        self.assertEqual(p1('))((((('), 3)
        self.assertEqual(p1('())'), -1)
        self.assertEqual(p1('))('), -1)
        self.assertEqual(p1(')))'), -3)
        self.assertEqual(p1(')())())'), -3)
    
    def test_p1(self):
        self.assertEqual(p1(self.d1data), 74)

    # Part 2 Tests
    def test_p2_examples(self):
        self.assertEqual(p2(')'), 1)
        self.assertEqual(p2('()())'), 5)
    
    def test_p2(self):
        self.assertEqual(p2(self.d1data), 1795)
