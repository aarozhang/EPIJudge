import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    # sort intervals
    # create a new named tuple to house a single endpoint
    Endpoint = collections.namedtuple('Endpoint', ('time', 'isStart'))
    endpoints = []
    for event in A:
        endpoints.append(Endpoint(event.start, True))
        endpoints.append(Endpoint(event.finish, False))

    # pythonic creation of end points
    # endpoints = [e for event in A
    #              for e in (Endpoint(event.start, True), Endpoint(event.finish, False))]

    endpoints.sort(key=lambda e: (e.time, not e.isStart))

    curr_events = 0
    result = 0
    for e in endpoints:
        if e.isStart:
            curr_events += 1
            result = max(result, curr_events)

        else:
            curr_events -= 1

    return result


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
