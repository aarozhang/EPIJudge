import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    keywords_counter = collections.Counter(keywords)
    remaining = len(keywords)
    result = Subarray(-1, -1)

    left = 0
    for right, w in enumerate(paragraph):
        if w in keywords:
            keywords_counter[w] -= 1
            if keywords_counter[w] == 0:
                remaining -= 1

        while remaining == 0:
            # collect result
            if result == Subarray(-1, -1) or right - left < result.end - result.start:
                result = Subarray(left, right)

            left_word = paragraph[left]
            if left_word in keywords:
                keywords_counter[left_word] += 1
                if keywords_counter[left_word] > 0:
                    remaining += 1

            left += 1

    return result


'''
keywords = {banana, cat}
[apple, banana, apple, apple, dog, cat, apple, dog, banana, apple, cat, dog]
        l
                                    r

remaining = 0
counter = {
    banana: 0
    cat: 0
}
["b", "c", "e"]
["a", "b", "c", "b", "a", "d", "c", "a", "e", "a", "a", "b", "e"]
                                     l
                                                              r

remaining = 0
counter = {
    b: 0
    c: 0
    e: 0
}
res = (3, 8)
'''


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    # print(find_smallest_subarray_covering_set(["a", "b", "c", "b", "a", "d", "c", "a", "e", "a", "a", "b", "e"], ["b", "c", "e"]))

    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
