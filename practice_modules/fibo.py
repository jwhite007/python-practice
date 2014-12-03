#!/usr/bin/env python

def fib(n):
    result = []
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
        result.append(a)
    return result


def fib_rec(n, a=1, b=1, result=[]):
    result.append(a)
    a, b = b, a + b
    if a > n:
        return result
    else:
        return fib_rec(n, a=a, b=b, result=result)

# def fib_rec2(a, b, n):
#     print a
#     a, b = b, a + b


if __name__ == '__main__':
    from timeit import timeit
    result = []
    # print(fib_rec(40))
    # print fib(40)
    setup = "from __main__ import fib_rec; result = []"
    fib = timeit(stmt="fib(40)", setup="from __main__ import fib", number=100000)
    fib_rec = timeit(stmt="fib_rec(1, 1, 40, result)", setup=setup, number=100000)
    print fib
    print fib_rec
    print fib / fib_rec
