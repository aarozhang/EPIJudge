from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    if not A:
        return -1

    l, r = 0, len(A) - 1

    while l < r:
        mid = (l + r) // 2

        if A[mid] < A[r]:
            r = mid
        else:
            l = mid + 1

    return l


'''
[5, 6, 7, 8, 9, 1, 2, 3, 4]
                m
'''


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
