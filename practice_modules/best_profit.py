#! /usr/bin/env python

def best_profit(alist):
    """
    This function takes a list of stock prices. The indexes are 'times'.
    The function calculates the max profit which could have be acheived by
    buying at at a specific time and selling at a specific time. Buy time,
    buy price, sell time, sell price, and max profit are returned.
    """

    max_profit = 0
    buy_time = 0
    buy_time2 = 0

    for i in range(len(alist)):
        if alist[i] < alist[buy_time]:
            buy_time2 = i
        else:
            if alist[i] - alist[buy_time2] > max_profit:
                buy_time = buy_time2
                buy_price = alist[buy_time2]
                (max_profit,
                 sell_time,
                 sell_price) = (alist[i] - alist[buy_time],
                                     i,
                                     alist[i])

    return 'buy time:\t' + str(buy_time) + '\n' + 'buy price:\t' + str(buy_price) +'\n' + 'sell time:\t' + str(sell_time) + '\n' + 'sell price:\t' + str(sell_price) + '\n' + 'max profit:\t' + str(max_profit)

if __name__ == '__main__':
    from timeit import timeit
    ALIST = [8, 13, 15, 10, 6, 7, 2, 11]
    # ALIST = [8, 13, 15, 10, 6, 7, 2, 11, 15]
    # ALIST = [8, 13, 15, 10, 6, 7, 2]

    print best_profit(ALIST)
    # print timeit(stmt='best_profit(ALIST)', setup='from __main__ import best_profit, ALIST')
