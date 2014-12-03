#! /usr/bin/env python


def handshakes(people):
    handshakes = 0
    while people > 1:
        people -= 1
        handshakes += people

    return handshakes


def handshakes_rec(people):
    handshakes = people - 1
    if people <= 1:
        return 0
    else:
        handshakes += handshakes_rec(people - 1)
        return handshakes

if __name__ == '__main__':
    print handshakes(5)
    # from timeit import timeit
    # from random import randrange
    # print timeit(stmt="handshakes(randrange(100))",
    #              setup="from __main__ import handshakes, randrange")
    # print timeit(stmt="handshakes_rec(randrange(100))",
    #              setup="from __main__ import handshakes_rec, randrange")
