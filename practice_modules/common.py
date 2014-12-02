#! /usr/bin/env python

from collections import defaultdict


def common(*args):
    args = list(args)
    for i in range(len(args)):
        args[i] = set(args[i])
    dd = defaultdict(int)
    l = []
    for i in args:
        for k in i:
            dd[k] += 1
    for key, val in dd.items():
        if val == len(args):
            l.append(key)
    return l


#without defaultdict
def common_wodd(*args):
    args = list(args)
    for i in range(len(args)):
        args[i] = set(args[i])
    d = {}
    l = []
    for i in args:
        for k in i:
            if k in d:
                d[k] += 1
            else:
                d[k] = 1
    for key, val in d.items():
        if val == len(args):
            l.append(key)
    return l

if __name__ == '__main__':
    l1 = [1, 2, 3, 8]
    l2 = [3, 4, 5, 8]
    l3 = [3, 6, 7, 8, 8]
    common(l1, l2, l3)
