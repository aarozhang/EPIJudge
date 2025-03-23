from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if not L:
        return None

    dummy = sublist_head = ListNode()
    sublist_head.next = L

    # find start of sublist
    for _ in range(start - 1):
        sublist_head = sublist_head.next

    # start reversal
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy.next


'''
     s         f
1 -> 2 -> 3 -> 4 -> 5
h    i    t

     s         f
1 -> 3 -> 2 -> 4 -> 5
h         i    t

     s         f
1 -> 4 -> 3 -> 2 -> 5
h              i    t
'''

if __name__ == '__main__':
    n5 = ListNode(5, None)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    res = reverse_sublist(n1, 2, 4)

    while res:
        print(res.data)
        res = res.next

    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
