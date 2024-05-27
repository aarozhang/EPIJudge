import math

from test_framework import generic_test


def parity(x: int) -> int:
    '''
    Brute force
    - Iterate bits one by one
    - perform x & 1 to check if least significant bit is a 1 or 0.
    - perform xor after the x & 1 to update res. Res will be a 0 for even count or 1 for odd count.
    - Then shift right one to check next bit.

    Time complexity is O(n) where n is the len of the bit representation of x

    res = 0
    while x:
        res ^= x & 1
        x >>= 1

    return res
    '''

    '''
    Optimized (approach 1):
    - Use a bit fiddling trick: x & (x - 1) removes the lowest set bit. A set bit is a bit == 1.
    
    Time complexity is O(k) where k is the number of set bits in x.
    
    res = 0
    while x:
        res ^= 1   # toggles res
        x &= x - 1 # drops lowest set bit
    
    return res
    '''

    res = 0
    while x:
        res ^= 1  # toggles res
        x &= x - 1  # erases lowest set bit

    return res


def variant_right_propagate_rightmost_set_bit(x: int) -> int:
    lsb = x & ~(x - 1)  # get rightmost set bit
    index = math.sqrt(lsb)  # get index of rightmost set bit

    # calculate bit to OR against
    bit = 0
    for i in range(int(index)):
        bit = (bit << 1) | 1  # adds 1 to right

    return x | int(bit)


if __name__ == '__main__':
    print(variant_right_propagate_rightmost_set_bit(80) == 95)

    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
