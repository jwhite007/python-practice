#! /usr/bin/env python
from collections import defaultdict


def rm_dupes(alist):
    dupe_dict = defaultdict(int)
    for i in alist:
        dupe_dict[i] += 1
    i = 0
    while i < len(alist):
        if dupe_dict[alist[i]] > 1:
            del alist[i]
            dupe_dict[alist[i]] -= 1
        else:
            i += 1
    return alist

if __name__ == '__main__':
    alist = ['a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd']
    print rm_dupes(alist)
