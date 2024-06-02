from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    if not A:
        return A

    A = A[::-1]
    carry = 1
    i = 0

    while i < len(A):
        sum = A[i] + carry
        A[i] = sum % 10

        if sum >= 10:
            i += 1
        else:
            carry = 0
            break

    # edge case: one last carry over
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
