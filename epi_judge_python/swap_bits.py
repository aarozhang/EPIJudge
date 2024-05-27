from test_framework import generic_test

'''
Brute force:
- Use a bitmask to extract ith and jth bits, save them to variables then swap values.
- Honestly this approach is not inefficient, but we can be smarter.

Optimized:
- Since bit values can only be 0 or 1. We can reduce unnecessary work in two ways...
- 1. Check that the two values even differ before swapping.
- 2. If the values differ, simply flip values to opposite.

Time complexity of both is O(1)
'''
def swap_bits(x, i, j):
    # check if bit values at i and j differ
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)  # create bit_mask with bit values of 1 at i and j indexes
        x ^= bit_mask  # flips values at i and j

    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
