from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    if not A:
        return []

    A = A[::-1] # reverse arr
    carry = 1
    i = 0
    while carry and i < len(A):
        total = carry + A[i]
        A[i] = total % 10
        carry = total // 10
        i += 1

    if carry:
        A.append(carry)

    return A[::-1]

'''
Examples:
[]
[9]
[1,2,9]
[9,9,9]
'''

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
