from unittest import TestCase

import aoc
from d12 import p1, p2


class D12_Test(TestCase):
    def setUp(self):
        super().setUp()
        self.given_data = aoc.d12data()

    # Part 1 Tests
    def test_p1_examples(self):
        self.assertEqual(p1('[1,2,3]'), 6)
        self.assertEqual(p1('{"a":2,"b":4}'), 6)
        self.assertEqual(p1('[[[3]]]'), 3)
        self.assertEqual(p1('{"a":{"b":4},"c":-1}'), 3)
        self.assertEqual(p1('{"a":[-1,1]}'), 0)
        self.assertEqual(p1('[-1,{"a":1}]'), 0)
        self.assertEqual(p1('[]'), 0)
        self.assertEqual(p1('{}'), 0)
    
    def test_p1(self):
        self.assertEqual(p1(self.given_data), 156366)

    # Part 2 Tests
    def test_p2_examples(self):
        self.assertEqual(p2('[1,2,3]'), 6)
        self.assertEqual(p2('[1,{"c":"red","b":2},3]'), 4)
        self.assertEqual(p2('{"d":"red","e":[1,2,3,4],"f":5}'), 0)
        self.assertEqual(p2('[1,"red",5]'), 6)
    
    def test_p2(self):
        self.assertEqual(p2(self.given_data), 96852)

