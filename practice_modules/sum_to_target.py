#! /usr/bin/env python
"""This module contains two functions, sum_two_to_target and sum_n_to_target."""

def sum_two_to_target(alist, target):
    """takes a list of real numbers and a target as arguments and returns all
    groups of two numbers in that list which sum to the target."""
    diff_dict = dict()
    for i in alist:
        # ensures that single elements added to themselves and equal to target
        # are not included.
        if (i == target - i) and alist.count(i) == 1:
            continue
        # ensures that multiple elements with equal value are only included once.
        if not i in diff_dict:
            diff_dict[target - i] = [i] + [target - i]
    blist = []
    for i in alist:
        if i in diff_dict:
            blist.append(diff_dict[i])
    for i in range(len(blist)):
        # Convert lists to tuples. Lists are not hashable, and set() works by
        # hashing.
        blist[i] = tuple(blist[i])
    # Convert list to a set which consists of unique elements (get rid of
    # multiples of the same element).
    aset = set(blist)
    # Convert set back to list for output... not completely necessary, could
    # just return set.
    blist = list(aset)
    # Convert lists back to tuples for output... not completely necessary,
    # could just return a list of tuples.
    for i in range(len(blist)):
        blist[i] = list(blist[i])
    return blist

def sum_n_to_target(n, alist, target):
    """takes a list of real numbers and a target as arguments and returns all
    groups of n numbers in that list which sum to the target."""
    diff_dict = dict()
    if n == 1:
        # Base case for recursive-call stack.
        if target in alist:
            return [[target]]
        else:
            return []
    else:
        for i in alist:
            clist = alist[:]
            clist.remove(i)
            # ensures that single elements added to themselves and equal to target
            # are not included
            if not target - i in diff_dict:
                # include i in each list element returned by the recursive call with
                # the complement as target
                diff_dict[target - i] = [[i] + j for j in sum_n_to_target(n - 1,
                                                                          clist,
                                                                          target - i)]
    blist = []
    # Check to see if compliments are contained in diff_dict. If so append
    # value to output list.
    for i in alist:
        if i in diff_dict:
            for j in diff_dict[i]:
                blist.append(j)
    for i in range(len(blist)):
        # Sort so that multiples of the same element will be recognized.
        blist[i].sort()
        # Convert lists to tuples. Lists are not hashable, and set() works by
        # hashing.
        blist[i] = tuple(blist[i])
    # Convert list to a set which consists of unique elements (get rid of
    # multiples of the same element).
    aset = set(blist)
    # Convert set back to a list which is needed for processing further up the
    # recursive call stack.
    blist = list(aset)
    for i in range(len(blist)):
        # Convert tuples back to lists which is needed for processing further up
        # the recursive call stack.
        blist[i] = list(blist[i])
    return blist

if __name__ == '__main__':
    # from timeit import timeit
    MYLIST = [1, 2, 3, 4.2, 5.8, 5, 5, 6, -15, 20]
    # MYLIST = [1, 3, 6, 4]
    print sum_two_to_target(MYLIST, 10)
    print sum_n_to_target(3, MYLIST, 10)
    # print timeit(stmt='sum_n_to_target(3, MYLIST, 10)',
    #              setup='from __main__ import sum_n_to_target, MYLIST', number=100000)
    # print timeit(stmt='sum_two_to_target(MYLIST, 10)',
    #              setup='from __main__ import sum_two_to_target, MYLIST', number=100000)
    # print timeit(stmt='sum_two_to_target2(MYLIST, 10)',
    #              setup='from __main__ import sum_two_to_target2, MYLIST', number=100000)