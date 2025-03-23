from typing import List

from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:
    def backtrack(curr, first_num):

        if len(curr) == k:
            result.append(curr.copy())
            return

        for i in range(first_num, n + 1):
            curr.append(i)
            backtrack(curr, i + 1)
            curr.pop()

    result = []
    backtrack([], 1)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
