from test_framework import generic_test


def square_root(k: int) -> int:
    l, r = 0, k
    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= k:
            l = mid + 1
        else:
            r = mid - 1

    return l - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
