from typing import List

from test_framework import generic_test


def get_max_trapped_water(heights: List[int]) -> int:
    left, right, max_amount = 0, len(heights) - 1, 0

    while left < right:
        max_amount = max(max_amount, min(heights[left], heights[right]) * (right - left))
        if heights[right] > heights[left]:
            left += 1
        else:
            right -= 1
        print(left, right, max_amount)

    return max_amount


'''
[1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1]
                      l
                                                    r
max = 8
'''



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
