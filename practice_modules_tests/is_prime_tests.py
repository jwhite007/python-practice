#! /usr/bin/env python

import unittest
from python_practice.practice_modules.is_prime import is_prime, is_prime2, is_prime3

class TestIsPrime(unittest.TestCase):

    def test_p2vp3(self):
        alist = range(1, 10001)
        self.assertListEqual(filter(is_prime2, alist), filter(is_prime3, alist))

    def test_is_prime(self):
        self.assertEqual(True, is_prime(11))

    def test_is_not_prime(self):
        self.assertNotEqual(True, is_prime(9))

    def test_output_list_of_primes_from_list(self):
        ALIST = range(1, 101)
        self.assertListEqual([1, 2, 3, 5, 7, 11, 13, 17,
                              19, 23, 29, 31, 37, 41, 43, 47,
                              53, 59, 61, 67, 71, 73, 79, 83, 89, 97],
                             filter(is_prime, ALIST))

    # def test_p2vp3(self):
    #     alist = range(1, 101)
    #     self.assertListEqual(filter(is_prime2, alist), filter(is_prime3, alist))

if __name__ == '__main__':
    unittest.main()
