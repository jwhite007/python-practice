#! /usr/bin/env python

import unittest
from practice_modules.min_max import report_max, report_min

class TestMinMax(unittest.TestCase):
    def setUp(self):
        self.ALIST = [42, 23, 6, 44, 78, 32, 47, 1, 100]

    def test_report_max(self):
        self.assertTupleEqual(report_max(self.ALIST), (100, 8))

    def test_report_min(self):
        self.assertTupleEqual(report_min(self.ALIST), (1, 7))

if __name__ == '__main__':
    unittest.main()
