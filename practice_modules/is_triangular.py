#! /usr/bin/env python


def is_triangular(n):
    n = n
    c = 1
    while n > c:
        n = n - c
        c = c + 1
    if n == c:
        return True
    if n < c:
        return False


def is_triangular_rec(n, c=1):
    if n == 0:
        return True
    elif n < 0:
        return False
    else:
        return is_triangular_rec(n - c, c=(c + 1))


def print_triangulars1(r):
    count = 0
    for l in range(1, r + 1):
        n = l
        c = 1
        while n > c:
            n = n - c
            c = c + 1
        if n == c:
            count += 1
            print count, l
    return ''


def print_triangulars2(r):
    count = 1
    n = 1
    while n <= r:
        print count, n
        count += 1
        n += count
    return ''


def print_triangulars3(r):
    l = []
    n = 0
    tn = 0
    while tn < r - n:
        n += 1
        tn = (n**2 + n) / 2
        l.append((n, tn))
    return l


def print_triangulars4(r):
    l = []
    for i in range(1, r + 1):
        if is_triangular(i):
            l.append(i)
    return l

if __name__ == '__main__':
    # print is_triangular(5)
    print is_triangular_rec(105)
    # print print_triangulars(100)
    # print print_triangulars_alt(100)
    # print print_triangulars_alt_alt(100)
    # print is_triangular_rec(105, 1)
    # import timeit
    # print timeit.timeit(stmt="is_triangular(105)",
    #                     setup="from __main__ import is_triangular",
    #                     number=1000000)
    # print timeit.timeit(stmt="is_triangular_rec(105, 1)",
    #                     setup="from __main__ import is_triangular_rec",
    #                     number=1000000)
    # print print_triangulars3(100)
