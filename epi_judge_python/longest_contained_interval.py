from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    unprocessed = set(A)
    longest_range = 0

    while unprocessed:
        curr = unprocessed.pop()
        left_val = curr - 1
        while left_val in unprocessed:
            unprocessed.remove(left_val)
            left_val -= 1

        right_val = curr + 1
        while right_val in unprocessed:
            unprocessed.remove(right_val)
            right_val += 1

        longest_range = max(longest_range, right_val - left_val - 1)

    return longest_range


'''
[1,2,3,5,6,7]
'''



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
