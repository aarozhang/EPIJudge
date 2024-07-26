from typing import List

from test_framework import generic_test


def minimum_total_waiting_time(service_times: List[int]) -> int:
    min_waiting_time = 0

    service_times.sort()
    for i, time in enumerate(service_times):
        remaining = len(service_times) - 1 - i
        min_waiting_time += time * remaining
    return min_waiting_time


if __name__ == '__main__':
    # print(minimum_total_waiting_time([1,2,3,5]))
    exit(
        generic_test.generic_test_main('minimum_waiting_time.py',
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
