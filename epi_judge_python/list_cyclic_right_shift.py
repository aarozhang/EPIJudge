from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if not L:
        return None

    # compute length of L and find the tail
    tail = L
    n = 1
    while tail.next:
        tail = tail.next
        n += 1

    # no processing needed
    k %= n
    if k == 0:
        return L

    # cycle shift logic start
    # connect tail to head
    tail.next = L
    # find new tail and disconnect
    new_tail = tail
    for _ in range(n - k):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head


'''
k = 3
1 -> 2 -> 3 -> 4 -> 5
     i

3 -> 4 -> 5 -> 1 -> 2
'''


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
