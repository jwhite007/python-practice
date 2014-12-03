#! /usr/bin/env python

import unittest
from practice_modules.best_profit import best_profit

class TestBestProfit(unittest.TestCase):
    def test_best_profit1(self):
        """tests best_profit when min buy price changes but max profit does not"""
        ALIST = [8, 13, 15, 10, 6, 7, 2]
        self.assertEqual(best_profit(ALIST),
                         'buy time:\t0\nbuy price:\t8\nsell time:\t2\nsell price:\t15\nmax profit:\t7')

    def test_best_profit2(self):
        """tests best_profit when min buy price changes and max profit changes thereafter"""
        ALIST = [8, 13, 15, 10, 6, 7, 2, 11]
        self.assertEqual(best_profit(ALIST),
                         'buy time:\t6\nbuy price:\t2\nsell time:\t7\nsell price:\t11\nmax profit:\t9')

    def test_best_profit3(self):
        """tests best_profit when min buy price changes and max profit changes twice thereafter"""
        ALIST = [8, 13, 15, 10, 6, 7, 2, 11, 15]
        self.assertEqual(best_profit(ALIST),
                         'buy time:\t6\nbuy price:\t2\nsell time:\t8\nsell price:\t15\nmax profit:\t13')

if __name__ == '__main__':
    unittest.main()