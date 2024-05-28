from test_framework import generic_test

'''
Brute force:
- use two pointers and iterate 32 least significant bits, swapping where necessary
- O(n) time where n is length of bit value
'''

def reverse_bits(x: int) -> int:
    # brute force approach
    res = 0
    shift = 63

    while x:
        res += (x & 1) << shift
        x >>= 1
        shift -= 1

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
