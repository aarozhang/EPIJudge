import collections

from test_framework import generic_test


def can_form_palindrome(s: str) -> bool:
    # sexy one-liner
    return sum(count % 2 for count in collections.Counter(s).values()) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
