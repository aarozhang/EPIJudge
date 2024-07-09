import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    # Forward iteration: remove b's and count number of a's
    a_count = 0
    write_idx = 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]  # write_idx will stay on b's and overwrite its b with s[i]'s val
            write_idx += 1
        if s[i] == 'a':
            a_count += 1

    # Backward iteration: replace a's with dd's
    curr = write_idx - 1  # index of last b
    write_idx += a_count - 1  # last index of needed space
    final_size = write_idx + 1

    while curr >= 0:
        if s[curr] == 'a':
            s[write_idx - 1:write_idx + 1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[curr]
            write_idx -= 1
        curr -= 1

    return final_size

'''
[a,c,d,c,a,c,a]
 i
   w
[d,d,c,d,c,d,d]             
'''

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
