#! /usr/bin/env python


def fact(n):
    fact = 1
    while n - 1 > 1:
        fact *= n
        n -= 1
    return fact


# def fact_rec(n):
#     if n - 1 > 1:
#         return n * fact_rec(n - 1)
#     return n


def fact_rec(n):
    if n == 0:
        return 1
    else:
        return n * fact_rec(n - 1)


def combo(n, r, order=True, repetition=True):
    if order:
        if repetition:
            return n**r
        else:
            return fact_rec(n) / fact_rec(n - r)
    else:
        if repetition:
            return fact_rec(n + r - 1) / (fact_rec(r) * fact_rec(n - 1))
        else:
            return fact_rec(n) / (fact_rec(n - r) * fact_rec(r))


if __name__ == '__main__':
    # from timeit import timeit
    # print fact(5)
    # print fact_rec(5)
    # print timeit(stmt="fact(5)",
    #              setup="from __main__ import fact")
    # print timeit(stmt="fact_rec(5)",
    #              setup="from __main__ import fact_rec")
    # print combo(2, 2, order=False, repetition=False)
    # print combo(4, 2, order=False)
    # print combo(4, 2, repetition=False)
    # print combo(4, 2)
    for i in xrange(2, 11):
        print combo(i, 2, order=False, repetition=False)
