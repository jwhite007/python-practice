#! /usr/bin/env python


def report_min(l):
    ci = 1
    i = 0
    count = 0
    while ci < len(l):
        if l[ci] < l[i]:
            i = ci
            ci = i + 1
        else:
            ci += 1
        count += 1
    return (l[i], count)


def report_min_fw(l):
    mn = l[0]
    count = 0
    for i in l[1:]:
        if i < mn:
            mn = i
        count += 1
    return (mn, count)


def report_max(l):
    ci = 1
    i = 0
    while ci < len(l):
        if l[ci] > l[i]:
            i = ci
            ci = i + 1
        else:
            ci += 1

    return l[i]

if __name__ == '__main__':
    # import random
    # l = random.sample(xrange(1, 101), 10)
    l = [1, 42, 23, 6, 44, 78, 32, 47, 1, 100]
    print l
    print report_min(l)
    print report_min_fw(l)
    # print min(l)
    # print report_max(l)
    # print max(l)
