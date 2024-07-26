from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    def backtrack(i):
        if i == len(A):
            result.append(partial.copy())
            return

        for num in A:
            if num not in partial:
                partial.append(num)
                backtrack(i + 1)
                partial.pop()

    partial = []
    result = []
    backtrack(0)
    return result


# this solution is a bit more intuitive.
def leetcode_solution(A: List[int]) -> List[List[int]]:
    def backtrack(curr):
        if len(curr) == len(A):
            result.append(curr.copy())
            return

        for num in A:
            if num not in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()

    result: List[List[int]] = []
    backtrack([])
    return result


if __name__ == '__main__':
    # print(permutations([1, 2, 3]))
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
