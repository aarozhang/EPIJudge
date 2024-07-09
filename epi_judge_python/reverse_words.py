import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    # helper to reverse words
    def reverse(start: int, end: int):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    # reverse string to get words in correct position
    reverse(0, len(s) - 1)

    # reverse letters in words
    left, right = 0, 0
    while right < len(s):
        if s[right] == ' ':
            reverse(left, right - 1)
            left = right + 1

        right += 1

    # reverse last word
    if left < right:
        reverse(left, right - 1)

    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
