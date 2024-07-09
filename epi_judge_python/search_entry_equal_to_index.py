import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def search_entry_equal_to_its_index(A: List[int]) -> int:
    if not A:
        return -1

    l, r = 0, len(A) - 1
    while l <= r:
        mid = (l + r) // 2

        if A[mid] == mid:
            return mid
        elif A[mid] > mid:
            r = mid - 1
        else:
            l = mid + 1

    return -1


def search_entry_equal_to_its_index_variant_1(A: List[int]) -> int:

    return -1


'''
[-4, 0, 1, 2, 4, 4, 5, 6]
                 m
[1, 1, 1, 1, 1, 1, 1]
          m

Since there is not clear logic to dictate whether to search left or right, the best time complexity we can achieve
is O(n) by simply traversing the array. However, there is a way to optimize our O(n) solution but incorporated skips 
based on the current element and it's index.
'''


@enable_executor_hook
def search_entry_equal_to_its_index_wrapper(executor, A):
    result = executor.run(functools.partial(search_entry_equal_to_its_index,
                                            A))
    if result != -1:
        if A[result] != result:
            raise TestFailure('Entry does not equal to its index')
    else:
        if any(i == a for i, a in enumerate(A)):
            raise TestFailure('There are entries which equal to its index')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_entry_equal_to_index.py',
            'search_entry_equal_to_index.tsv',
            search_entry_equal_to_its_index_wrapper))
