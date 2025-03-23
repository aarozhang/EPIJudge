from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if not L:
        return None

    dummy = ListNode(0, L)
    tail = dummy.next

    # get length of list and find tail
    n = 1
    while tail.next:
        tail = tail.next
        n += 1

    # print(it.data)
    # if shift is same as length, return initial head
    k = k % n
    if k == 0:
        return L

    # connect tail to head
    tail.next = dummy.next

    # calculate distance of new head from curr head
    new_head_distance = n - k

    it = dummy
    for _ in range(new_head_distance):
        it = it.next

    print(it.data)

    dummy.next = it.next
    it.next = None
    return dummy.next

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
