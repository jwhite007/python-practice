#! /usr/bin/env python
import timeit


def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins


def recDC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change-i,
                                 knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins


def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


def main():
    amnt = 63
    clist = [1, 5, 10, 25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for", amnt, "requires")
    print(dpMakeChange(clist, amnt, coinCount, coinsUsed), "coins")
    print("They are:")
    printCoins(coinsUsed, amnt)
    print("The used list is as follows:")
    print(coinsUsed)
    print(len(coinsUsed))

    # dpMakeChange(clist, amnt, coinCount, coinsUsed)
    # return None


def dpMakeChange2(coinValueList, change, minCoins):
    for cents in range(change+1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j]+1 < coinCount:
                coinCount = minCoins[cents-j]+1
        minCoins[cents] = coinCount
    for i in range(len(minCoins)):
        print str(i) + ': ' + str(minCoins[i])
    return minCoins[change]


def dpMakeChange3(coinValueList, change, minCoins):
    for cents in range(change+1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if cents - j == 0:
                coinCount = minCoins[cents-j]+1
            else:
                if minCoins[cents-j] == 0:
                    coinCount = 0
                else:
                    if minCoins[cents-j]+1 < coinCount:
                        coinCount = minCoins[cents-j]+1
        if cents < min(coinValueList):
            minCoins[cents] = 0
        else:
            minCoins[cents] = coinCount
    for i in range(len(minCoins)):
        print str(i) + ': ' + str(minCoins[i])
    return minCoins[change]


if __name__ == '__main__':
    # print timeit.timeit(stmt='recMC([1, 5, 10, 25], 63)',
    #                     setup='from __main__ import recMC',
    #                     number=1)
    # print timeit.timeit(stmt='recDC([1,5,10,25],63,[0]*64)',
    #                     setup='from __main__ import recDC',
    #                     number=1000)
    # print timeit.timeit(stmt='main()',
    #                     setup='from __main__ import main',
    #                     number=1000)
    cvl = [5, 8, 10, 25]
    amt = 18
    mcl = [0]*(amt + 1)
    print(dpMakeChange3(cvl, amt, mcl))
    # main()
    # print recMC([5, 8, 10, 25], 14)
