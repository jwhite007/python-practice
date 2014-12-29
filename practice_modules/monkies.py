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

result = 0
while result < 0.1:
    result = score('methinks it is like a weasel', generate_one(28))
print(result)
