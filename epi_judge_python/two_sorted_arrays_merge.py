from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    a, b, write_idx = m - 1, n - 1, m + n - 1
    while a >= 0 and b >= 0:
        if A[a] < B[b]:
            A[write_idx] = B[b]
            b -= 1
        else:  # A[a] >= B[b]:
            A[write_idx] = A[a]
            a -= 1

        write_idx -= 1

    while b >= 0:
        A[write_idx] = B[b]
        b, write_idx = b - 1, write_idx - 1

    return


'''
[3,3,3,3,4,11,17,20, ]
a
   w
[1,2,4,17,20]
   b
'''


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    arr_A = [3, 13, 17, 0, 0, 0, 0, 0]
    arr_B = [3, 7, 11, 19]
    merge_two_sorted_arrays(arr_A, 3, arr_B, len(arr_B))
    print(arr_A)

    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
