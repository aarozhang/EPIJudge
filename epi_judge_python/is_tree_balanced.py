import collections

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    def check_balance(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)

        left_res = check_balance(tree.left)
        if not left_res.balanced:
            return left_res

        right_res = check_balance(tree.right)
        if not right_res.balanced:
            return right_res

        is_balanced = abs(left_res.height - right_res.height) <= 1
        height = max(left_res.height, right_res.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balance(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
