#! /usr/bin/env python


def report_min(alist):
    index_of_min = 0
    for i in range(len(alist)):
        if alist[i] < alist[index_of_min]:
            index_of_min = i
    return (alist[index_of_min], index_of_min)

def report_max(alist):
    index_of_max = 0
    for i in range(len(alist)):
        if alist[i] > alist[index_of_max]:
            index_of_max = i
    return (alist[index_of_max], index_of_max)

if __name__ == '__main__':
    from timeit import timeit
    import random
    ALIST = random.sample(xrange(1, 101), 10)
    print ALIST
    # ALIST = [42, 23, 6, 44, 78, 32, 47, 1, 100]
    # print report_min(ALIST)
    print report_max(ALIST)
    # print timeit(stmt='report_min(l)', setup='from __main__ import report_min, ALIST')
    # print timeit(stmt='report_min_fw(l)', setup='from __main__ import report_min_fw, ALIST')
    # print min(l)
    # print report_max(l)
    # print max(l)
