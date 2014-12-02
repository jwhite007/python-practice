#! /usr/bin/env python

def best_profit(alist):
    max_profit = 0
    buy_time = 0
    sell_time = 0
    for i in range(len(alist)):
        for j in range(i, len(alist)):
            if alist[j] - alist[i] > max_profit:
                max_profit, buy_time, sell_time = alist[j] - alist[i], i, j

    return buy_time, sell_time, max_profit

def best_profit2(alist):
    max_profit = 0
    buy_time = 0
    buy_price = 0
    sell_time = 0
    sell_price = 0
    for i in range(len(alist)):
        if alist[i] < alist[buy_time]:
            buy_time = i
            buy_price = alist[i]
        else:
            if alist[i] - alist[buy_time] > max_profit:
                (max_profit,
                 sell_time,
                 sell_price) = (alist[i] - alist[buy_time],
                                     i,
                                     alist[i])

    return 'buy time:\t' + str(buy_time) + '\n' + 'buy price:\t' + str(buy_price) +'\n' + 'sell time:\t' + str(sell_time) + '\n' + 'sell price:\t' + str(sell_price) + '\n' + 'max profit:\t' + str(max_profit)

if __name__ == '__main__':
    from timeit import timeit
    ALIST = [8, 13, 15, 10, 6, 7, 2, 11]
    print best_profit(ALIST)
    print best_profit2(ALIST)
    # print timeit(stmt='best_profit(ALIST)', setup='from __main__ import best_profit, ALIST')
    # print timeit(stmt='best_profit2(ALIST)', setup='from __main__ import best_profit2, ALIST')