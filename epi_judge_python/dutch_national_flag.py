import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    '''
    Optimized approach 1: Two pointer with two passes
    pivot_val = A[pivot_index]

    left = 0
    for i in range(len(A)):
        if A[i] < pivot_val:
            A[left], A[i] = A[i], A[left]
            left += 1

    right = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] > pivot_val:
            A[right], A[i] = A[i], A[right]
            right -= 1

    '''

    '''
    Optimized approach 2: three pointers one pass
    
    pivot_val = A[pivot_index]

    l, r, mid = 0, len(A), 0

    while mid < r:
        if A[mid] < pivot_val:
            A[mid], A[l] = A[l], A[mid]
            mid += 1
            l += 1
        elif A[mid] > pivot_val:
            r -= 1
            A[mid], A[r] = A[r], A[mid]
        else:
            mid += 1
    '''
    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
