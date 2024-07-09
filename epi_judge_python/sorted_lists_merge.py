from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:

    dummy = tail = ListNode()

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next = L1
            tail = L1
            L1 = L1.next
        elif L1.data > L2.data:
            tail.next = L2
            tail = L2
            L2 = L2.next

    if L1:
        tail.next = L1
    elif L2:
        tail.next = L2

    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
