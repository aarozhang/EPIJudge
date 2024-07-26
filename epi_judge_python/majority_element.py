from typing import Iterator

from test_framework import generic_test


def majority_search(stream: Iterator[str]) -> str:
    count, maj_element = 0, ''
    for element in stream:
        if count == 0:
            maj_element = element
            count += 1
        elif element == maj_element:
            count += 1
        else:
            count -= 1
    return maj_element


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
