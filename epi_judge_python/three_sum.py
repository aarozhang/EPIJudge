from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()

    for i in range(len(A)):
        j, k = i, len(A) - 1

        while j <= k:
            if A[i] + A[j] + A[k] == t:
                return True
            elif A[i] + A[j] + A[k] < t:
                j += 1
            else:
                k -= 1

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
