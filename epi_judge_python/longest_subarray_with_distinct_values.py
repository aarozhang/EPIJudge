from typing import List, Dict

from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    element_to_index: Dict[int, int] = {}
    left = 0
    result = 0

    for right, element in enumerate(A):
        if element in element_to_index:
            if element_to_index[element] >= left:
                result = max(result, right - left)
                left = element_to_index[element] + 1

        element_to_index[element] = right

    return max(result, len(A) - left)


'''
[f, s, f, e, t, w, e, n, w, e]
 l
 r
'''


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
