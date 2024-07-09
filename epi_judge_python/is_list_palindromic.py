from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if not L:
        return True

    # find halfway point
    slow = fast = L
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    # reverse second half
    iter = slow.next
    while iter and iter.next:
        temp = iter.next
        iter.next = temp.next
        temp.next = slow.next
        slow.next = temp

    # check equality of two halves
    first_half, second_half = L, slow.next
    while second_half:
        if first_half.data != second_half.data:
            return False
        else:
            first_half, second_half = first_half.next, second_half.next

    return True


'''
1 -> 2 -> 3 -> 4 -> 5
          s
                    f
'''


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
