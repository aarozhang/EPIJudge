import functools

from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    # check if s is a substr
    if len(s) > len(t):
        return -1

    # create hash codes for substring of t and s
    base = 26
    t_hash = functools.reduce(lambda h, c: h * base + ord(c), t[:len(s)], 0)
    s_hash = functools.reduce(lambda h, c: h * base + ord(c), s, 0)
    power_s = base ** max(len(s) - 1, 0)

    # print(t_hash)
    # print(s_hash)
    # print(power_s)

    return 0


if __name__ == '__main__':
    print(rabin_karp('GACGCCA', 'CGC'))
    # exit(
    #     generic_test.generic_test_main('substring_match.py',
    #                                    'substring_match.tsv', rabin_karp))
