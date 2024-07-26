from typing import List, Dict

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    word_to_latest_i: Dict[str, int] = {}
    nearest_distance = float('inf')
    for i, word in enumerate(paragraph):
        if word in word_to_latest_i:
            nearest_distance = min(nearest_distance, i - word_to_latest_i[word])

        word_to_latest_i[word] = i

    return int(nearest_distance if nearest_distance != float('inf') else -1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
