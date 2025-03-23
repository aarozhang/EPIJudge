import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle(head: ListNode) -> Optional[ListNode]:
    if not head:
        return None

    # given two pointers at the same node, traverse the cycle and get length
    def get_cycle_len(start_node, iter_node):
        length = 1
        iter_node = iter_node.next

        while start_node is not iter_node:
            iter_node = iter_node.next
            length += 1

        return length

    # check if cycle
    slow_iter = fast_iter = head
    cycle_len = 0
    while fast_iter and fast_iter.next:
        slow_iter, fast_iter = slow_iter.next, fast_iter.next.next
        # cycle found
        if slow_iter is fast_iter:
            cycle_len = get_cycle_len(slow_iter, fast_iter)
            break

    if cycle_len == 0:
        return

    cycle_head_iter = advanced_iter = head

    for _ in range(cycle_len):
        advanced_iter = advanced_iter.next

    while cycle_head_iter is not advanced_iter:
        cycle_head_iter, advanced_iter = cycle_head_iter.next, advanced_iter.next

    return cycle_head_iter



@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))
