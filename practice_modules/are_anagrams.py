#! /usr/bin/env python
from collections import defaultdict

def are_anagrams(string1, string2):
    # big-O = 2n + 26 = n
    c1 = [0]*26
    c2 = [0]*26

    for i in string1:
        pos = ord(i) - ord('a')
        c1[pos] += 1

    for i in string2:
        pos = ord(i) - ord('a')
        c2[pos] += 1

    for i in range(len(c1)):
        if c1[i] != c2[i]:
            return False
    return True


def are_anagrams2(string1, string2):
    # same as are_anagrams2 but using defaultdict
    c1 = defaultdict(int)
    c2 = defaultdict(int)

    for i in string1:
        pos = ord(i) - ord('a')
        c1[pos] += 1

    for i in string2:
        pos = ord(i) - ord('a')
        c2[pos] += 1

    for i in range(len(c1)):
        if c1[i] != c2[i]:
            return False
    return True

def are_anagrams3(string1, string2):
    # big-O = n(n + n) = 2n^2 = n^2
    if len(string1) != len(string2):
        return False
    for i in string1:
        s1count = 0
        s2count = 0
        for k in string1:
            if i == k:
                s1count += 1
        for k in string2:
            if i == k:
                s2count += 1
        if s1count != s2count:
            return False
    return True

if __name__ == '__main__':
    import timeit
    # print timeit.timeit(stmt="are_anagrams3('dashed', 'shadedd')",
    #                     setup="from __main__ import are_anagrams3",
    #                     number=1000)
    # print timeit.timeit(stmt="are_anagrams3('dashed', 'fucked')",
    #                     setup="from __main__ import are_anagrams3",
    #                     number=1000)
    print timeit.timeit(stmt="are_anagrams('mississippi', 'ippississim')",
                        setup="from __main__ import are_anagrams",
                        number=100000)
    print timeit.timeit(stmt="are_anagrams2('mississippi', 'ippississim')",
                        setup="from __main__ import are_anagrams2",
                        number=100000)
    print timeit.timeit(stmt="are_anagrams3('mississippi', 'ippississim')",
                        setup="from __main__ import are_anagrams3",
                        number=100000)
    # print are_anagrams3('blab', 'albb')