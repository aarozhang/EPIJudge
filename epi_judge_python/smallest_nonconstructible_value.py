from typing import List

from test_framework import generic_test


def smallest_nonconstructible_value(A: List[int]) -> int:
    smallest_nonconstructible = 0
    for a in sorted(A):
        if a > smallest_nonconstructible + 1:
            break
        smallest_nonconstructible += a

    return smallest_nonconstructible + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
