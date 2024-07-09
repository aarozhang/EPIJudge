from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    if not L:
        return None

    dummy = advanced_iter = ListNode(0, L)

    for _ in range(k+1):
        advanced_iter = advanced_iter.next

    iter = dummy
    while advanced_iter:
        iter, advanced_iter = iter.next, advanced_iter.next

    iter.next = iter.next.next

    return dummy.next


'''
k = 3
d -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
               i                   a
'''


if __name__ == '__main__':
    # n6 = ListNode(6, None)
    # n5 = ListNode(5, n6)
    # n4 = ListNode(4, n5)
    # n3 = ListNode(3, n4)
    # n2 = ListNode(2, n3)
    # n1 = ListNode(1, n2)
    # remove_kth_last(n1, 3)
    #
    # while n1:
    #     print(n1.data)
    #     n1 = n1.next

    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
