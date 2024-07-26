import collections
import functools
import operator
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def find_minimum_visits(intervals: List[Interval]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=operator.attrgetter('right'))
    visit_time, res = intervals[0].right, 1
    for interval in intervals:
        if visit_time < interval.left:
            res += 1
            visit_time = interval.right
    return res


@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_points_covering_intervals.py',
            'minimum_points_covering_intervals.tsv',
            find_minimum_visits_wrapper))
