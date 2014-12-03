#! /usr/bin/env python

def rev_string(string):
    rev_string = ''
    for i in string:
        rev_string = i + rev_string
    return rev_string

def rev_string_rec(string):
    if len(string) == 1:
        return string
    return rev_string_rec(string[1:]) + string[0]

def rev_list(alist):
    blist = []
    for i in alist:
        blist = [i] + blist
    return blist

def rev_list_rec(alist):
    if len(alist) == 1:
        return alist
    else:
        return rev_list(alist[1:]) + alist[:1]

if __name__ == '__main__':
    from timeit import timeit
    ALIST = [1, 2, 3, 4]
    # print rev_list(ALIST)
    # print rev_list_rec(ALIST)
    # print rev_string('string')
    # print timeit(stmt="rev_string('string')", setup='from __main__ import rev_string')
    # print timeit(stmt="rev_string_rec('string')", setup='from __main__ import rev_string_rec')
    print timeit(stmt="rev_list(ALIST)", setup='from __main__ import rev_list, ALIST')
    print timeit(stmt="rev_list_rec(ALIST)", setup='from __main__ import rev_list_rec, ALIST')
    print timeit(stmt='ALIST[::-1]', setup='from __main__ import ALIST')
