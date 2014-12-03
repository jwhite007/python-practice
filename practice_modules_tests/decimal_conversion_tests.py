#! /usr/bin/env python

import unittest
from practice_modules.decimal_conversion import dec_to_base

class TestDecimalToBase(unittest.TestCase):

    def test_dec_to_bin(self):
        self.assertEqual(dec_to_base(100, 2), '1100100')

    def test_dec_to_hex(self):
        self.assertEqual(dec_to_base(100, 16), '64')

    def test_dec_to_oct(self):
        self.assertEqual(dec_to_base(100, 8), '144')

if __name__ == '__main__':
    unittest.main()