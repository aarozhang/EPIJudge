from functools import lru_cache
from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    if not A:
        return False

    furthest = 0
    last_index = len(A) - 1

    i = 0
    while i <= furthest and furthest < last_index:
        furthest = max(furthest, i + A[i])
        i += 1

    return furthest >= last_index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
