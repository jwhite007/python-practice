#! /usr/bin/env python


def seq_search(l, n):
    i = 0
    found = False
    while i < len(l) and not found:
        if l[i] == n:
            found = True
        i += 1
    return found


# def bin_search(l, n):
#     # import pdb; pdb.set_trace()
#     mid = len(l) // 2
#     found = False
#     while len(l) > 0 and not found:
#         if n == l[mid]:
#             found = True
#         elif n < l[mid]:
#             l = l[:mid]
#             mid = len(l) // 2
#         else:
#             l = l[mid + 1:]
#             mid = len(l) // 2

#     return found

def bin_search(l, n):
    first = 0
    last = len(l) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if n == l[mid]:
            found = True
        elif n < l[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return found


def bin_search_rec(l, n):
    if len(l) == 0:
        return False
    else:
        mid = len(l) // 2
        if l[mid] == n:
            return True
        else:
            if l[mid] > n:
                return bin_search_rec(l[:mid], n)
            else:
                return bin_search_rec(l[mid + 1:], n)


if __name__ == '__main__':
    from timeit import timeit
    from random import randrange
    # l = [1, 2, 3, 4]
    # print seq_search(l, 3)
    # print seq_search(l, 5)
    # print bin_search(l, 1)
    # print bin_search(l, 4)
    l = range(100001)
    print timeit(stmt="seq_search(l, randrange(10001))",
                 setup="from __main__ import seq_search, l, randrange",
                 number=10000)
    print timeit(stmt="bin_search(l, randrange(100001))",
                 setup="from __main__ import bin_search, l, randrange",
                 number=10000)
    # print timeit(stmt="bin_search_rec(l, randrange(100001))",
    #              setup="from __main__ import bin_search_rec, l, randrange",
    #              number=10000)

