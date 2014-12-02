#! /usr/bin/env python


class BinHeap(object):
    def __init__(self):
        self.heaplist = [0]
        self.size = 0

    def get_size(self):
        return self.size

    def perc_up(self, i):
        """'Problem Solving with Algorithms and Data Structures' version"""
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                (self.heaplist[i],
                 self.heaplist[i // 2]) = (self.heaplist[i // 2],
                                           self.heaplist[i])
            i = i - 1

    def insert1(self, k):
        """my version (faster than insert2)"""
        self.heaplist.append(k)
        self.size += 1
        i = self.size
        while self.heaplist[i] < self.heaplist[i // 2]:
            if i // 2 == 0:
                break
            (self.heaplist[i],
                 self.heaplist[i // 2]) = (self.heaplist[i // 2],
                                           self.heaplist[i])
            i = i // 2

    def insert2(self, k):
        """'Problem Solving with Algorithms and Data Structures' version"""
        self.heaplist.append(k)
        self.size += 1
        self.perc_up(self.size)

    def perc_down(self, i):
        """'Problem Solving with Algorithms and Data Structures' version"""
        while i * 2 <= self.size:
            minc = self.min_child(i)
            if self.heaplist[i] > self.heaplist[minc]:
                (self.heaplist[i],
                 self.heaplist[minc]) = (self.heaplist[minc],
                                                self.heaplist[i])
            i = minc

    def min_child(self, i):
        """'Problem Solving with Algorithms and Data Structures' version"""
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def pop_min(self):
        """'Problem Solving with Algorithms and Data Structures' version"""
        ret_val = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size]
        self.heaplist.pop()
        self.size -= 1
        self.perc_down(1)
        return ret_val

    def build_heap1(self, alist):
        """my version"""
        for i in alist:
            self.insert1(i)

    # def build_heap2(self, alist):
    #     """ slower than build_heap1 """
    #     for i in alist:
    #         self.insert2(i)

    def build_heap2(self, alist):
        """'Problem Solving with Algorithms and Data Structures' version
        faster than build_heap1 """
        self.size = len(alist)
        i = self.size // 2
        self.heaplist.extend(alist[:])
        while i > 0:
            self.perc_down(i)
            i -= 1

    def show_heap(self):
        """my addition"""
        return self.heaplist[1:]

if __name__ == '__main__':
    from random import randrange
    from timeit import timeit
    ALIST = [8, 20, 2, 4, 7, 25, 1]
    # ALIST = []
    # for index in range(21):
    #     ALIST.append(randrange(1, 21))
    BH1 = BinHeap()
    BH2 = BinHeap()
    for _ in ALIST:
        BH1.insert1(_)
        BH2.insert2(_)
    # print timeit(stmt='BH1.build_heap1(ALIST)', setup='from __main__ import BH1, ALIST', number=100)
    # print timeit(stmt='BH2.build_heap2(ALIST)', setup='from __main__ import BH2, ALIST', number=100)
    print timeit(stmt='BH1.insert1(-1)', setup='from __main__ import BH1, ALIST', number=1000)
    print timeit(stmt='BH2.insert2(-1)', setup='from __main__ import BH2, ALIST', number=1000)
