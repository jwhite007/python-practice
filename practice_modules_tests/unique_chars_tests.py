#! /usr/bin/env python

import unittest
from unique_chars import unique, unique_chars


class TestUniqueChars(unittest.TestCase):

    def test_unique_true(self):
        self.assertTrue(unique('string'))

    def test_unique_false(self):
        self.assertFalse(unique('mississippi'))

    def test_unique_chars(self):
        self.assertListEqual(['s', 't', 'r', 'i', 'n', 'g'],
                             unique_chars('string'))

    def test_unique_chars_one_unique(self):
        self.assertListEqual(['m'], unique_chars('mississippi'))



if __name__ == '__main__':
    unittest.main()
