from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    left_chars = []
    pairs = {'(': ')', '{': '}', '[': ']'}

    for c in s:
        if c in pairs:
            left_chars.append(c)
        elif left_chars and pairs[left_chars[-1]] == c:
            left_chars.pop()
        else:
            return False

    return True if len(left_chars) == 0 else False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
