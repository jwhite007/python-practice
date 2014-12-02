#! /usr/bin/env python

from collections import defaultdict


def unique(string):
    for i in string:
        for k in string[string.index(i) + 1:]:
            if k == i:
                return False
    return True


# def unique_chars(string):
#     l = []
#     for i in string:
#         count = 0
#         for k in string[string.index(i) + 1:]:
#             if k == i:
#                 count += 1
#         if count == 0:
#             l.append(i)
#     return l


def unique_chars(string):
    l = []
    done = False
    for i in string:
        for k in string[string.index(i) + 1:]:
            if k == i:
                done = True
                break
        if done:
            done = False
            continue
        l.append(i)
    return l


def unique_chars2(string):
    d = defaultdict(int)
    l = []
    for i in string:
        d[i] += 1
    for key, val in d.items():
        if val == 1:
            l.append(key)
    return l


def unique_chars3(string):
    d = dict()
    l = []
    for i in string:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for key, val in d.items():
        if val == 1:
            l.append(key)
    return l

if __name__ == '__main__':
    # print unique_chars3('ththis')
    import timeit
    print timeit.timeit(stmt="unique_chars2('mississippi')",
                        setup="from __main__ import unique_chars2",
                        number=1000000)
    print timeit.timeit(stmt="unique_chars3('mississippi')",
                        setup="from __main__ import unique_chars3",
                        number=1000000)
