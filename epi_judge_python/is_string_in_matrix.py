import functools
from typing import List

from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    @functools.lru_cache(None)
    def search_pattern(x, y, offset) -> bool:
        if offset == len(pattern):
            return True

        if (not (0 <= x < len(grid) and 0 <= y < len(grid[x]))) or grid[x][y] != pattern[offset]:
            return False

        return any(
                search_pattern(next_x, next_y, offset + 1)
                for next_x, next_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        )

    return any(
        search_pattern(i, j, 0) for i in range(len(grid)) for j in range(len(grid[i]))
    )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
