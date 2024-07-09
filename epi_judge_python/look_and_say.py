import itertools

from test_framework import generic_test


def look_and_say(n: int) -> str:
    s = '1'

    # itertools.groupby() will group elements by key. We can then construct our output str by getting the count + key.
    for _ in range(n - 1):
        s = ''.join(
            str(len(list(group))) + key for key, group in itertools.groupby(s)
        )

    return s


'''
n = 6
[1, 11, 21, 1211, 111221, 312211] -> 1
'''

if __name__ == '__main__':
    #print(look_and_say(6))
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))


# BOOK SOLUTION
# def look_and_say(n: int) -> str:
#     if n < 1:
#         return ''
#
#     # helper
#     def next_nums(s):
#         substr, i = [], 0
#         # generate next string based on curr s length, starting from beginning
#         while i < len(s):
#             count = 1
#
#             # count current grouping of numbers
#             while i + 1 < len(s) and s[i] == s[i + 1]:
#                 count += 1
#                 i += 1
#
#             substr.append(str(count) + s[i])
#             i += 1
#             print(substr)
#
#         return ''.join(substr)
#
#     res = '1'
#     for _ in range(1, n):
#         res = next_nums(res)
#         print(res)
#
#     return res


# PYTHONIC SOLUTION
# def look_and_say(n: int) -> str:
#     s = '1'
#
#     # itertools.groupby() will group elements by key. We can then construct our output str by getting the count + key.
#     for _ in range(n - 1):
#         s = ''.join(
#             str(len(list(group))) + key for key, group in itertools.groupby(s)
#         )
#
#     return s