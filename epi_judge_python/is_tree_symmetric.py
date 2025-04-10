from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def check_symmetric(tree0, tree1):
        if not tree0 and not tree1:
            return True

        elif tree0 and tree1:
            return (tree0.data == tree1.data
                    and check_symmetric(tree0.left, tree1.right)
                    and check_symmetric(tree0.right, tree1.left))

        return False

    return check_symmetric(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
