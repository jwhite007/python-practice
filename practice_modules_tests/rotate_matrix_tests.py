#! /usr/bin/env python

import unittest
from practice_modules import rotate_matrix


class TestRotateMatrix(unittest.TestCase):

    def setUp(self):
        self.r1 = ['a', 'b', 'c']
        self.r2 = ['d', 'e', 'f']
        self.r3 = ['g', 'h', 'i']
        self.r4 = ['j', 'k', 'l']
        self.r5 = ['m', 'n', 'o', 'p']
        self.r6 = ['q', 'r', 's', 't']
        self.r7 = ['u', 'v', 'w', 'x']
        self.r8 = ['y', 'z', 'aa', 'bb']
        self.r9 = ['a1', 'a2', 'a3', 'a4', 'a5']
        self.r10 = ['b1', 'b2', 'b3', 'b4', 'b5']
        self.r11 = ['c1', 'c2', 'c3', 'c4', 'c5']
        self.r12 = ['d1', 'd2', 'd3', 'd4', 'd5']
        self.r13 = ['e1', 'e2', 'e3', 'e4', 'e5']

    def test_rotate(self):
        self.assertListEqual([['g', 'd', 'a'],
                             ['h', 'e', 'b'],
                             ['i', 'f', 'c']],
                             rotate_matrix.rotate_square_matrix(self.r1,
                                                                self.r2,
                                                                self.r3))

    def test_too_many_rows(self):
        self.assertRaises(rotate_matrix.SizeError,
                          rotate_matrix.rotate_square_matrix,
                          self.r1, self.r2, self.r3, self.r4)

    def test_extra_col_in_row(self):
        with self.assertRaises(rotate_matrix.SizeError):
            rotate_matrix.rotate_square_matrix(self.r1, self.r2,
                                               self.r3, self.r5)

    def test_rotate_in_place_with_rot(self):
        self.assertListEqual([['g', 'd', 'a'],
                             ['h', 'e', 'b'],
                             ['i', 'f', 'c']],
                             rotate_matrix.rotate_square_matrix_in_place_with_rot(self.r1,
                                                                         self.r2,
                                                                         self.r3))

    def test_rotate_in_place_with_rot_var(self):
        self.assertListEqual([['g', 'd', 'a'],
                             ['h', 'e', 'b'],
                             ['i', 'f', 'c']],
                             rotate_matrix.rotate_square_matrix_in_place_with_rot_var(self.r1,
                                                                                      self.r2,
                                                                                      self.r3))

    def test_rotate_in_place_with_rot_var_4x4(self):
        self.assertListEqual([['y', 'u', 'q', 'm'],
                             ['z', 'v', 'r', 'n'],
                             ['aa', 'w', 's', 'o'],
                             ['bb', 'x', 't', 'p']],
                             rotate_matrix.rotate_square_matrix_in_place_with_rot_var(self.r5,
                                                                                      self.r6,
                                                                                      self.r7,
                                                                                      self.r8))

    def test_rostate_in_place_with_rot_var_5x5(self):
        self.assertListEqual([['e1', 'd1', 'c1', 'b1', 'a1'],
                              ['e2', 'd2', 'c2', 'b2', 'a2'],
                              ['e3', 'd3', 'c3', 'b3', 'a3'],
                              ['e4', 'd4', 'c4', 'b4', 'a4'],
                              ['e5', 'd5', 'c5', 'b5', 'a5']],
                              rotate_matrix.rotate_square_matrix_in_place_with_rot_var(self.r9,
                                                                                      self.r10,
                                                                                      self.r11,
                                                                                      self.r12,
                                                                                      self.r13))

    def test_rotate_by_rev_and_trans(self):
        self.assertListEqual([['g', 'd', 'a'],
                             ['h', 'e', 'b'],
                             ['i', 'f', 'c']],
                             rotate_matrix.rotate_matrix_by_rev_and_trans(self.r1,
                                                                          self.r2,
                                                                          self.r3))

    def test_rotate_rec_matrix_by_rev_and_trans(self):
        self.assertListEqual([['u', 'q', 'm'],
                              ['v', 'r', 'n'],
                              ['w', 's', 'o'],
                              ['x', 't', 'p']],
                              rotate_matrix.rotate_matrix_by_rev_and_trans(self.r5,
                                                                           self.r6,
                                                                           self.r7))

if __name__ == "__main__":
    unittest.main()
