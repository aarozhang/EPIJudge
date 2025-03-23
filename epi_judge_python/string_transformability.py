import collections
import string
from typing import Set

from test_framework import generic_test


def transform_string(D: Set[str], s: str, t: str) -> int:
    StringWithDistance = collections.namedtuple('StringWithDistance', ('candidate_string', 'distance'))
    q = collections.deque([StringWithDistance(s, 0)])
    D.remove(s)

    while q:
        curr_str, distance = q.popleft()
        if curr_str == t:
            return distance

        for i in range(len(curr_str)):
            for c in string.ascii_lowercase:
                cand = curr_str[:i] + c + curr_str[i + 1:]
                if cand in D:
                    D.remove(cand)
                    q.append(StringWithDistance(cand, distance + 1))

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
