from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    if n < 1:
        return []

    # initialize result array
    res = [[1] * (i+1) for i in range(n)]

    for i in range(n):
        for j in range(1, i):
            res[i][j] = res[i-1][j-1] + res[i-1][j]

    return res


if __name__ == '__main__':
    # print(generate_pascal_triangle(5))
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
