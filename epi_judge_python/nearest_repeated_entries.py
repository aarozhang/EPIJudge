from typing import List, Dict

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    word_to_latest_index: Dict[str, int] = {}
    nearest_distance = float('inf')

    for i, word in enumerate(paragraph):
        if word in word_to_latest_index:
            latest_index = word_to_latest_index[word]
            nearest_distance = min(nearest_distance, i - latest_index)

        word_to_latest_index[word] = i

    return int(nearest_distance) if nearest_distance != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
