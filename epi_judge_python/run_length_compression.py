from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    res = []

    start = 0
    for i in range(len(s)):
        if s[i].isdigit():
            continue
        else:
            count = int(s[start:i])
            res.append(count * s[i])

            start = i + 1

    return ''.join(res)


'''
'12a3b4c'
'''


def encoding(s: str) -> str:
    res = []

    count = 0
    for i in range(len(s)):
        if i == 0 or s[i] == s[i-1]:
            count += 1
        else:
            res.append(str(count) + s[i-1])
            count = 1

    res.append(str(count) + s[len(s) - 1])

    return ''.join(res)


'''
aaabbcccc
'''

def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    # print(decoding('2a10b5c'))
    # print(encoding('abcdddd'))
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
