from typing import List

from epi_judge_python.sorted_arrays_merge import merge_sorted_arrays
from test_framework import generic_test


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    # decompose input A into sorted increasing arrays
    sorted_subarrays = []
    increasing, decreasing = range(2)
    subarray_type = increasing
    start_idx = 0
    for i in range(1, len(A) + 1):
        if i == len(A) or ((A[i - 1] < A[i] and subarray_type == decreasing)
                or (A[i-1] >= A[i] and subarray_type == increasing)):
            sorted_subarrays.append(A[start_idx:i] if subarray_type == increasing else A[i - 1:start_idx - 1:-1])
            start_idx = i
            subarray_type = (decreasing if subarray_type == increasing else increasing)

    return merge_sorted_arrays(sorted_subarrays)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
