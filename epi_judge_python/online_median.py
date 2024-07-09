import heapq
from typing import Iterator, List

from test_framework import generic_test


def online_median(sequence: Iterator[int]) -> List[float]:
    min_heap: List[int] = []  # upper half
    max_heap: List[int] = []  # lower half. values are negative
    res = []

    for x in sequence:
        # push x to upper half. take smallest from upper and push to lower
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))

        # heaps should be even if num of elements is even. Otherwise, have min_heap be larger.
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        res.append(0.5 * (min_heap[0] + -max_heap[0]) if len(min_heap) == len(max_heap) else min_heap[0])

    return res


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
