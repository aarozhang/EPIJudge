import heapq
import itertools
from typing import Iterator, List

from test_framework import generic_test


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    min_heap: List[int] = []

    for _ in range(k):
        heapq.heappush(min_heap, next(sequence))

    res = []
    while min_heap:
        element = heapq.heappop(min_heap)
        res.append(element)
        next_element = next(sequence, None)
        if next_element is not None:
            heapq.heappush(min_heap, next_element)

    return res


'''
[3, -1, 2, 6, 4, 5, 8] k = 2
'''


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
