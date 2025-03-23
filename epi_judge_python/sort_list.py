from typing import Optional

from epi_judge_python.sorted_lists_merge import merge_two_sorted_lists
from list_node import ListNode
from test_framework import generic_test


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    if L is None or L.next is None:
        return L

    # find midpoint of current list
    pre_slow, slow, fast = None, L, L
    while fast and fast.next:
        pre_slow = slow
        fast, slow = fast.next.next, slow.next

    # disconnect front half from back half
    if pre_slow:
        pre_slow.next = None

    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
