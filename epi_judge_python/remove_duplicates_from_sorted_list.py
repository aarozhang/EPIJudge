from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    dummy = ListNode(0, L)
    curr = dummy.next

    while curr and curr.next:
        while curr.next and curr.data == curr.next.data:
            curr.next = curr.next.next

        curr = curr.next

    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
