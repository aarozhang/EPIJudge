from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return None

    even_dummy, odd_dummy = ListNode(), ListNode()
    tails, turn = [even_dummy, odd_dummy], 0

    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1

    tails[0].next = odd_dummy.next
    tails[1].next = None
    return even_dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
