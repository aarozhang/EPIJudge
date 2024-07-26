import heapq
from typing import List, Tuple

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:

    min_heap: List[Tuple[int, int]] = []

    sorted_array_iterators = [iter(x) for x in sorted_arrays]

    for i, it in enumerate(sorted_array_iterators):
        element = next(it, None)
        if element is not None:
            heapq.heappush(min_heap, (element, i))

    res = []
    while min_heap:
        min_element, index = heapq.heappop(min_heap)
        res.append(min_element)
        new_element = next(sorted_array_iterators[index], None)
        if new_element is not None:
            heapq.heappush(min_heap, (new_element, index))

    return res


'''
input:
[3, 5, 7]
[0, 6]
[0, 6, 28]

output:
[0, 0, 3, 5, 6, 7, 28
'''


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
