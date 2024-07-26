import functools

from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    @functools.lru_cache(None)
    def compute_paths(x, y):
        if x == y == 0:
            return 1

        ways_top = 0 if x == 0 else compute_paths(x - 1, y)
        ways_left = 0 if y == 0 else compute_paths(x, y - 1)
        return ways_top + ways_left

    return compute_paths(n - 1, m - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
