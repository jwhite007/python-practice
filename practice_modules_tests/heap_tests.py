#! /usr/bin/env python

import unittest
from python_practice.practice_modules.heap import BinHeap
from random import randrange


class TestBinHeap(unittest.TestCase):

    def test_compare_inserts(self):
        alist = []
        for _ in range(1001):
            alist.append(randrange(1, 1001))
        bh1 = BinHeap()
        bh2 = BinHeap()
        for _ in alist:
            bh1.insert1(_)
            bh2.insert2(_)
        self.assertListEqual(bh1.show_heap(), bh2.show_heap())

if __name__ == '__main__':
    unittest.main()
