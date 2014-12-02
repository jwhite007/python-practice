#!/usr/bin/python


def sum(seq):
    def add(x, y):
        return x+y
    return reduce(add, seq, 0)

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    print sum(l)
