import collections
from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    origin_color = image[x][y]
    print(image[x][y])
    image[x][y] = not image[x][y]
    print(image[x][y])
    q = collections.deque([(x, y)])

    while q:
        curr_x, curr_y = q.popleft()
        for next_x, next_y in [(curr_x - 1, curr_y), (curr_x + 1, curr_y), (curr_x, curr_y - 1), (curr_x, curr_y + 1)]:
            if 0 <= next_x < len(image) and 0 <= next_y < len(image[next_x]) and image[next_x][next_y] == origin_color:
                image[next_x][next_y] = not image[next_x][next_y]
                q.append((next_x, next_y))

    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
