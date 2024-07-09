from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True

    def check_symmetry(subtree0, subtree1):
        if not subtree0 and not subtree1:
            return True
        elif subtree0 and subtree1:
            return (subtree0.data == subtree1.data and check_symmetry(subtree0.left, subtree1.right)
                    and check_symmetry(subtree0.right, subtree1.left))

        # one null one present is not symmetric
        return False

    return check_symmetry(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
