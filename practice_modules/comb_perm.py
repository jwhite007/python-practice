#! /usr/bin/env python


def fact(n):
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact

def fact1(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
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


def comb_perm(n, r, order=True, repetition=True):
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
    from timeit import timeit
    # for i in xrange(2, 11):
    #     print comb_perm(i, 2, order=False, repetition=False)
    # print comb_perm(5, 2, order=False, repetition=False)
    print(timeit(stmt = 'fact(5)', setup = 'from __main__ import fact'))
    print(timeit(stmt = 'fact1(5)', setup = 'from __main__ import fact1'))
    print(timeit(stmt = 'fact_rec(5)', setup = 'from __main__ import fact_rec'))
