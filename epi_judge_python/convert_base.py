import functools
import string

from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # helper to convert base 10 int to new base
    def convert_from_int(num: int, base: int) -> str:
        if num == 0:
            return '0'

        is_neg = False
        if num < 0:
            is_neg = True
            num *= -1

        res = []
        while num:
            digit = num % base
            res.append(string.hexdigits[digit].upper())
            num //= base

        if is_neg:
            res.append('-')

        return ''.join(res[::-1])

    negative = num_as_string[0] == '-'

    # convert num back to base ten int
    num_as_int = 0
    for i in range(len(num_as_string)):
        if num_as_string[i] == '-':
            continue

        num_as_int = num_as_int * b1 + string.hexdigits.index(num_as_string[i].lower())

    return convert_from_int(-1 * num_as_int, b2) if negative else convert_from_int(num_as_int, b2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))

# def convert_base(num_as_string: str, b1: int, b2: int) -> str:
#     # helper to convert base 10 int to new base
#     def convert_from_int(num: int, base: int) -> str:
#         if num == 0:
#             return '0'
#
#         is_neg = False
#         if num < 0:
#             is_neg = True
#             num *= -1
#
#         res = []
#         while num:
#             digit = num % base
#             res.append(string.hexdigits[digit].upper())
#             num //= base
#
#         if is_neg:
#             res.append('-')
#
#         return ''.join(res[::-1])
#
#     negative = num_as_string[0] == '-'
#
#     # convert num back to base ten int
#     num_as_int = 0
#     for i in range(len(num_as_string)):
#         if num_as_string[i] == '-':
#             continue
#
#         num_as_int = num_as_int * b1 + string.hexdigits.index(num_as_string[i].lower())
#
#     return convert_from_int(-1 * num_as_int, b2) if negative else convert_from_int(num_as_int, b2)