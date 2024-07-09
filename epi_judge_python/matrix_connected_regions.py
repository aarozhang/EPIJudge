import collections
from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    origin_color = image[x][y]
    image[x][y] = not image[x][y]
    q = collections.deque([(x, y)])

    while q:
        curr_x, curr_y = q.popleft()

        for new_x, new_y in ((curr_x - 1, curr_y), (curr_x + 1, curr_y), (curr_x, curr_y - 1), (curr_x, curr_y + 1)):
            if 0 <= new_x < len(image) and 0 <= new_y < len(image[new_x]) and image[new_x][new_y] == origin_color:
                image[new_x][new_y] = not image[new_x][new_y]
                q.append((new_x, new_y))

    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
