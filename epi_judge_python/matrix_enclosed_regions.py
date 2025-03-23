import collections
from typing import List

from test_framework import generic_test


def fill_surrounded_regions(board: List[List[str]]) -> None:
    n, m = len(board), len(board[0])
    # print(n, m)
    q = collections.deque([])

    # prime q with border cells
    for i in range(m):
        q.append((0, i))
        q.append((n - 1, i))

    for i in range(n):
        q.append((i, 0))
        q.append((i, m - 1))

    # print(q)

    while q:
        x, y = q.popleft()
        if board[x][y] == 'W':
            board[x][y] = 'T'
            for next_x, next_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]):
                    q.append((next_x, next_y))

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'W':
                board[i][j] = 'B'
            elif board[i][j] == 'T':
                board[i][j] = 'W'

    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
