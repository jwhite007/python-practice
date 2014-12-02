#! /usr/bin/env python

import unittest
from python_practice.practice_modules.are_anagrams import are_anagrams

class TestAreAnagrams(unittest.TestCase):
    def test_are_anagrams(self):
        self.assertEqual(True, are_anagrams('mississippi', 'ippississim'))

    def test_are_not_anagrams(self):
        self.assertNotEqual(True, are_anagrams('this', 'that'))

if __name__ == '__main__':
    unittest.main()