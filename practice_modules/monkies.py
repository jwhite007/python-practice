#! /usr/bin/env python3

import random

def generate_one(strlen):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    res = ''
    for _ in range(strlen):
        res = res + alphabet[random.randrange(27)]
    return res

def score(goal, test_string):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == test_string[i]:
            numSame = numSame + 1
    return numSame / len(goal)
# print(score('methinks it is like a weasel', generate_one(28)))

if __name__ == '__main__':
    from timeit import timeit

    def test_func(n):
        result = 0
        while result < n:
            result = score('methinks it is like a weasel', generate_one(28))
        return result

    print(timeit(stmt = 'test_func(0.1)', setup = 'from __main__ import test_func', number = 1))
    print(timeit(stmt = 'test_func(0.2)', setup = 'from __main__ import test_func', number = 1))
    print(timeit(stmt = 'test_func(0.3)', setup = 'from __main__ import test_func', number = 1))
