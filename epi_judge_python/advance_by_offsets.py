from functools import lru_cache
from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    max_index = 0
    i = 0
    while i < len(A):
        if i > max_index:
            break

        if max_index >= len(A) - 1:
            return True

        max_index = max(max_index, i + A[i])
        i += 1

    return False

'''
[3, 3, 1, 0, 0, 0, 1]
                i
i = 5
max = 4
'''

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))


# BOOK SOLUTION
# def can_reach_end(A: List[int]) -> bool:
#     if not A:
#         return False
#
#     furthest = 0
#     last_index = len(A) - 1
#
#     i = 0
#     while i <= furthest and furthest < last_index:
#         furthest = max(furthest, i + A[i])
#         i += 1
#
#     return furthest >= last_index


# MY CODED SOLUTION
# def can_reach_end(A: List[int]) -> bool:
#     max_index = 0
#     i = 0
#     while i < len(A):
#         if i > max_index:
#             break
#
#         if max_index >= len(A) - 1:
#             return True
#
#         max_index = max(max_index, i + A[i])
#         i += 1
#
#     return False