#! /usr/bin/env python

import unittest
from practice_modules.reverse import rev_string, rev_list, rev_string_rec, rev_list_rec

class TestReverse(unittest.TestCase):

    def test_rev_string(self):
        self.assertEqual(rev_string('string'), 'gnirts')

    def test_rev_string_rec(self):
        self.assertEqual(rev_string_rec('string'), 'gnirts')

    def test_rev_list(self):
        self.assertListEqual(rev_list([1, 2, 3, 4]), [4, 3, 2, 1])

    def test_rev_list_rec(self):
        self.assertListEqual(rev_list_rec([1, 2, 3, 4]), [4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()
