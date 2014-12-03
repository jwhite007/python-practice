#! /usr/bin/env python

def mcnuggets(n):
    x = 6
    y = 9
    z = 20
    if n == 0:
        return True
    for i in [x, y, z]:
        if n >= i and mcnuggets(n - i):
            return True
    return False


def mcnuggets2(n):
    # import pdb
    # pdb.set_trace()
    minmc = [0] * (n + 1)
    mlist = [6, 9, 20]
    for i in range(n + 1):
        mCount = i
        for j in [c for c in mlist if c <= i]:
            if minmc[i-j]+1 < mCount:
                mCount = minmc[i-j]+1
        minmc[i] = mCount
    for i in range(len(minmc)):
        print str(i) + ': ' + str(minmc[i])
    return minmc[n]


class Accumulator(object):
    pass

def mcnuggets_rec(n):
    x = 20
    y = 9
    z = 6
    xcount = Accumulator()
    ycount = Accumulator()
    zcount = Accumulator()
    xcount.val = 0
    ycount.val = 0
    zcount.val = 0

    def rec(n):
        if n == 0:
            return True
        for i in [x, y, z]:
            if n >= i and rec(n - i):
                if i == x:
                    xcount.val += 1
                elif i == y:
                    ycount.val += 1
                elif i == z:
                    zcount.val += 1
                return True
        return False

    if rec(n) is False:
        return False
    else:
        return '20*' + str(xcount.val) + ' + 9*' + str(ycount.val) + ' + 6*' + str(zcount.val)

if __name__ == "__main__":

    # for i in range(1, 201):
        # print 'mcnuggets(' + str(i) + '): ' + str(mcnuggets_rec(i))

    mcnuggets2(35)
