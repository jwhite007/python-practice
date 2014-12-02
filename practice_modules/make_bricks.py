#! /usr/bin/env python


def make_bricks(small, big, goal):
    """ without recursion """
    if big*5 <= goal:
        if goal - big*5 <= small:
            return True
        else:
            return False
    elif big*5 > goal:
        if goal % 5 <= small:
            return True
        else:
            return False


def make_bricks_rec(small, big, goal):
    """ with recursion """
    # import pdb; pdb.set_trace()
    if goal == 0:
        return True
    for i in [5, 1]:
        if i == 5 and big == 0:
            continue
        elif i == 1 and small == 0:
            continue
        elif i == 5:
            if goal >= i and make_bricks_rec(small, big - 1, goal - i):
                return True
        elif i == 1:
            if goal >= i and make_bricks_rec(small - 1, big, goal - i):
                return True
    return False


if __name__ == '__main__':
    # print make_bricks(1, 5, 21)
    # print "expect True: " + str(make_bricks_rec(2, 5, 26))
    # print "expect False: " + str(make_bricks_rec(2, 6, 33))
    import sys
    argone = sys.argv[1]
    # print make_bricks_rec(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    print argone
