from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    # goal is to find the first index where the value is >= the remaining citations
    citations.sort()
    n = len(citations)
    for i, c in enumerate(citations):
        if c >= n - i:
            return n - i

    return 0


'''
[1, 2, 2, 3, 5, 6]
 6  5  4  3  2  1
'''


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
