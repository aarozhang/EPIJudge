from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    if not prices:
        return 0.0

    buy, sell = 0, 0
    max_profit = 0.0

    while sell < len(prices):
        if prices[sell] < prices[buy]:
            buy = sell
        elif buy == sell:
            sell += 1
        else:
            max_profit = max(max_profit, prices[sell] - prices[buy])
            sell += 1

    return max_profit
'''
[3, 4, 2, 6, 7, 2, 1]
                   b
                      s
max = 5
[5, 4, 3, 2, 1]

O(n) time, O(1) space
'''

if __name__ == '__main__':
    # print(buy_and_sell_stock_once([3, 4, 2, 6, 7, 2, 1]) == 5.0)
    # print(buy_and_sell_stock_once([5, 4, 3, 2, 1]) == 0.0)
    # print(buy_and_sell_stock_once([3, 4, 6, 7]) == 4.0)
    # print(buy_and_sell_stock_once([3]) == 0.0)

    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
