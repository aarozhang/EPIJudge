from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if not x:
        return '0'

    # check if negative
    negative = False
    if x < 0:
        negative = True
        x *= -1

    res = []
    while x:
        digit = x % 10
        res.append(str(digit))
        x //= 10

    if negative:
        res.append('-')

    return ''.join(reversed(res))


def string_to_int(s: str) -> int:
    # check if negative
    neg = False
    if s[0] == '-':
        neg = True

    res = 0
    for i in range(len(s)):
        if s[i] == '+' or s[i] == '-':
            continue

        res = res * 10 + int(s[i])

    if neg:
        res *= -1

    return res


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
