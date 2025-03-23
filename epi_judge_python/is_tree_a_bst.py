from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def are_keys_in_range(tree, low_range=float('-inf'), high_range=float('inf')):
        if not tree:
            return True
        elif not low_range <= tree.data <= high_range:
            return False

        return are_keys_in_range(tree.left, low_range, tree.data) and are_keys_in_range(tree.right, tree.data, high_range)

    return are_keys_in_range(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
