#! /usr/bin/env python

from copy import deepcopy

# non-in-place rotations:
#   rotate +90:
#       reverse rows, transpose
#       or
#       transpose, reverse columns
#   rotate 180:
#       reverse rows, columns
#       or
#       reverse columns, rows
#   rotate -90:
#       reverse columns, transpose
#       or
#       transpose, reverse rows


def rotate_square_matrix(*args):
    for l in args:
        if len(l) != len(args[0]):
            raise SizeError('Lists do not represent an NxN matrix')
    if len(args[0]) != len(args):
        raise SizeError('Lists do not represent an NxN matrix')

    m = list(args)
    ml = []

    for row in m:
        ml.append(row)
    mlr = deepcopy(ml)

    for row in range(len(m)):
        for col in range(len(m[0])):
            mlr[col][(len(args) - 1) - row] = ml[row][col]
    return mlr


def rotate_square_matrix_in_place_with_rot(*args):
    # rotate +90 by rotating outer square, followed by inner squares

    for l in args:
        if len(l) != len(args[0]):
            raise SizeError('Lists do not represent an NxN matrix')
    if len(args[0]) != len(args):
        raise SizeError('Lists do not represent an NxN matrix')

    m = list(args)
    row = 0
    col = 0
    rowl = len(m[0])
    cp = m[0][0]
    count = 0
    length = len(m) - 1
    breakout = False

    while breakout is False:
        if count < 4:
            ncp = m[col][(rowl - 1) - row]
            m[col][(rowl - 1) - row] = cp
            cp = ncp
            # d = col
            # col = (rowl - 1) - row
            # row = d
            col, row = (rowl - 1) - row, col
            count += 1
        if count == 4:
            col += 1
            if row == len(m) / 2:
                breakout = True
            elif col == length:
                row += 1
                col = row
                length -= 1
            cp = m[row][col]
            count = 0
    return m


def rotate_square_matrix_in_place_with_rot_var(*args):
        for l in args:
            if len(l) != len(args[0]):
                raise SizeError('Lists do not represent an NxN matrix')
        if len(args[0]) != len(args):
            raise SizeError('Lists do not represent an NxN matrix')

        m = list(args)
        row = 0
        col = 0
        rowl = len(m[0])
        # cp = m[0][0]
        width = len(m) - 1

        while row <= rowl / 2:
            while col < width:
                cp = m[row][col]
                count = 0
                while count < 4:
                    ncp = m[col][(rowl - 1) - row]
                    m[col][(rowl - 1) - row] = cp
                    cp = ncp
                    col, row = (rowl - 1) - row, col
                    count += 1
                col += 1
            width -= 1
            row += 1
            col = row
        return m


def rotate_square_matrix_by_rev_and_transpose(*args):
    # rotate +90

    for l in args:
        if len(l) != len(args[0]):
            raise SizeError('Lists do not represent an NxN matrix')
    if len(args[0]) != len(args):
        raise SizeError('Lists do not represent an NxN matrix')

    m = list(args)

    # reverse rows
    mrev = []
    row = len(m) - 1
    while row >= 0:
        mrev.append(m[row])
        row -= 1

    # build rotated place-holder matrix
    mrot = deepcopy(mrev)

    # transpose
    row = 0
    while row < len(mrev):
        col = 0
        while col < len(mrev[0]):
            mrot[col][row] = mrev[row][col]
            col += 1
        row += 1
    return mrot


def rotate_square_matrix_in_place_by_rev_and_trans(*args):
    # rotate +90

    # reverse rows
    m = list(args)
    mfrow = 0
    mtrow = len(m[0]) - 1

    while mfrow < mtrow:
        ph = m[mtrow]
        m[mtrow] = m[mfrow]
        m[mfrow] = ph
        mfrow += 1
        mtrow -= 1

    # transpose
    row = 0
    col = 1
    breakout = False

    while breakout is False:
        if row == len(m) - 1 and col == len(m[0]):
            breakout = True
        elif col == len(m[0]):
            row += 1
            col = row + 1
        else:
            ph = m[col][row]
            m[col][row] = m[row][col]
            m[row][col] = ph
            col += 1

    return m



def rotate_matrix_by_rev_and_trans(*args):
    # rotate +90

    for l in args:
        if len(l) != len(args[0]):
            raise SizeError('Lists do not represent matrix')
    m = list(args)

    # reverse rows
    mrev = []
    row = len(m) - 1
    while row >= 0:
        mrev.append(m[row])
        row -= 1

    # build rotated place-holder matrix
    mrot = [[i for i in range(len(m))] for i in range(len(m[0]))]

    # mrot = []
    # for i in m[0]:
    #     l = []
    #     for k in range(len(m)):
    #         l.append(k)
    #     mrot.append(l)

    # transpose [row][col] = [col][row]
    row = 0
    while row < len(mrev):
        col = 0
        while col < len(mrev[0]):
            mrot[col][row] = mrev[row][col]
            col += 1
        row += 1
    return mrot


class SizeError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


if __name__ == '__main__':
    r1 = ['a', 'b', 'c']
    r2 = ['d', 'e', 'f']
    r3 = ['g', 'h', 'i']
    r4 = ['j', 'k', 'l']
    r5 = [1, 2, 3, 4]
    r6 = [5, 6, 7, 8]
    r7 = [9, 10, 11, 12]
    r8 = [13, 14, 15, 16]
    r9 = [17, 18, 19, 20]
    r10 = [21, 22, 23, 24]
    # print [r1, r2, r3]
    # print rotate_square_matrix(r1, r2, r3)
    # print rotate_square_matrix_in_place(r1, r2, r3)
    # print rotate_square_matrix_by_rev_and_transpose(r1, r2, r3)
    # print rotate_square_matrix_in_place_by_rev_and_trans(r1, r2, r3)
    # print rotate_square_matrix_in_place_by_rev_and_trans(r5, r6, r7, r8)
    print r7
    print r8
    print r9
    print r10
    for l in rotate_square_matrix(r7, r8, r9, r10):
        print l
