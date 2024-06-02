from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:

    # first calculate max profit that can be made by day i
    daily_profits_pre = [0.0] * len(prices)
    min_price = float('inf')
    max_profit = 0.0

    for i, price in enumerate(prices):
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
        daily_profits_pre[i] = max_profit

    # now calculate max profit that can be made after day i
    daily_profits_post = [0.0] * len(prices)
    max_price = float('-inf')
    max_profit = 0.0

    for i, price in enumerate(reversed(prices)):
        max_price = max(max_price, price)
        max_profit = max(max_profit, max_price - price)
        daily_profits_post[i] = max_profit

    # find max after combining values at ith index from both arrays
    res = 0.0
    for i in range(len(daily_profits_post)):

        res = max(res, daily_profits_pre[i] + daily_profits_post[len(prices) - 1 - i])

    return res

'''
[12, 11, 13, 9, 12, 8, 14, 13, 15]

post = [7,7,7,7,7,2,2,0]
'''

if __name__ == '__main__':
    # print(buy_and_sell_stock_twice([12, 11, 13, 9, 12, 8, 14, 13, 15]))
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
