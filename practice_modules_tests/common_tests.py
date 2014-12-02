#! /usr/bin/env python

import unittest
from practice_modules.common import common, common_wodd


class TestCommon(unittest.TestCase):

    def setUp(self):
        self.l1 = [1, 2, 3, 8]
        self.l2 = [3, 4, 5, 8]
        self.l3 = [3, 6, 7, 8, 8]

    def test_common(self):
        self.assertListEqual([3, 8], common(self.l1, self.l2, self.l3))

    def test_common_wodd(self):
        self.assertListEqual([3, 8], common_wodd(self.l1,
                                                        self.l2,
                                                        self.l3))

if __name__ == '__main__':
    unittest.main()
