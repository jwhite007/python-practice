#! /usr/bin/env python


def is_prime(num):
    i = 2
    while num // i >= i:
        if num % i == 0:
            return False
        i += 1
    return True

if __name__ == "__main__":
    # from timeit import timeit
    # print is_prime(2)
    ALIST = range(1, 101)
    print filter(is_prime, ALIST)
