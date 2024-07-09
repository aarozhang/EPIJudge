from typing import List

from test_framework import generic_test


# O(log n) time
def search_first_of_k(A: List[int], k: int) -> int:
    left, right, res = 0, len(A) - 1, -1

    while left <= right:
        mid = (left + right) // 2

        if A[mid] < k:
            left = mid + 1
        elif A[mid] > k:
            right = mid - 1
        else:
            right = mid - 1
            res = mid

    return res


'''
[-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        m  

- use binary search to find an occurrence of the key.
- If key exists, remove the right half to continue the search.
- continue searching until search constraint is exhausted.
'''

'''
Variant 1:
Find the first occurrence of an element greater than the key. Even if the key does not exist,
return the next greatest element.
'''


def search_first_of_k_variant_1(A: List[int], k: int) -> int:
    if not A:
        return -1

    l, r, res = 0, len(A) - 1, -1
    mid = -1

    while l <= r:
        mid = (l + r) // 2

        if A[mid] < k:
            l = mid + 1
        elif A[mid] > k:
            r = mid - 1
        else:  # A[mid] == k
            res = mid  # store right most occurrence's index
            l = mid + 1

    # edge case: if key does not exist, assign mid (index of closest value less than k)
    if res == -1:
        res = mid if A[mid] < k else mid - 1

    # edge case: if no greater element exists
    return res + 1 if res + 1 < len(A) else -1


if __name__ == '__main__':
    # Variant 1 Tests
    # print(search_first_of_k_variant_1([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 285))
    # print(search_first_of_k_variant_1([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], -13))
    # print(search_first_of_k_variant_1([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 402))
    # print(search_first_of_k_variant_1([1], 0))
    # print(search_first_of_k_variant_1([], 0))

    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
