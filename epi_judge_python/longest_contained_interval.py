from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    unprocessed = set(A)
    longest = 0

    for num in A:
        if num in unprocessed:
            left, right = num - 1, num + 1
            unprocessed.remove(num)

            while left in unprocessed:
                unprocessed.remove(left)
                left -= 1

            while right in unprocessed:
                unprocessed.remove(right)
                right += 1

            longest = max(longest, right - left - 1)

    return longest


'''
[1,2,3,5,6,7]
'''



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
