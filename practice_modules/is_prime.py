#! /usr/bin/env python


def is_prime(num):
    i = 2
    while num // i >= i:
        if num % i == 0:
            return False
        i += 1
    return True


def is_prime2(num):
    for i in range(2, num // 2 + 1):
        if num % i != 0:
            continue
        else:
            return False
    return True


def is_prime3(num):
    for i in range(2, num):
        if num % i != 0:
            continue
        else:
            return False
    return True

if __name__ == "__main__":
    # from timeit import timeit
    # print is_prime(2)
    ALIST = range(1, 101)
    print filter(is_prime, ALIST)
    # print filter(is_prime5, ALIST)
