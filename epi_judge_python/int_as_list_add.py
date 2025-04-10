from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    carry = 0
    dummy = iter = ListNode()

    while L1 or L2 or carry:
        val = carry + (L1.data if L1 else 0) + (L2.data if L2 else 0)
        iter.next = ListNode(val % 10)
        iter = iter.next
        carry = val // 10
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None

    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
