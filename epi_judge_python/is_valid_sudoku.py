import math
from typing import List

from test_framework import generic_test


def is_valid_sudoku(board: List[List[int]]) -> bool:
    # helper
    def has_duplicates(block: List) -> bool:
        values = list(filter(lambda x: x != 0, block))
        return len(values) != len(set(values))

    # check rows and cols
    n = len(board)
    if any(
        has_duplicates([board[i][j] for j in range(n)])
        or has_duplicates([board[j][i] for j in range(n)])
        for i in range(n)
    ):
        return False

    # check regions
    region_size = int(math.sqrt(n))
    return all(
        not has_duplicates([
            board[a][b]
            for a in range(I * region_size, (I + 1) * region_size)
            for b in range(J * region_size, (J + 1) * region_size)]
        ) for I in range(region_size) for J in range(region_size)
    )


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku_commented_solution(board: List[List[int]]) -> bool:
    # helper: checks if given r,c, or block has dups
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))  # collect all non zeroes
        return len(block) != len(set(block))  # by converting to a set, we can check for dups

    n = len(board)

    # check row and cols
    if any(
            has_duplicate([board[i][j] for j in range(n)])  # rows
            or has_duplicate([board[j][i] for j in range(n)])  # cols
            for i in range(n)):
        return False

    # check regions
    region_size = int(math.sqrt(n))  # region_size = 3
    return all(
            not has_duplicate([
                board[a][b]
                for a in range(region_size * I, region_size * (I + 1))
                for b in range(region_size * J, region_size * (J + 1))
            ]) for I in range(region_size) for J in range(region_size)
    )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
