from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    # helper to check if substring is valid ip address.
    # returns true, is single digit val or substr does not have leading zeroes and is within range of 0 to 255.
    def is_valid(substr):
        return len(substr) == 1 or (substr[0] != '0' and int(substr) <= 255)

    res = []
    segments = [''] * 4
    for i in range(1, min(4, len(s))):
        segments[0] = s[:i]

        if is_valid(segments[0]):
            for j in range(1, min(len(s) - i, 4)): # range of i + 1 to i + 4
                segments[1] = s[i:i + j]

                if is_valid(segments[1]):
                    for k in range(1, min(len(s) - i - j, 4)):
                        segments[2], segments[3] = s[i + j:i + j + k], s[i + j + k:]

                        if is_valid(segments[2]) and is_valid(segments[3]):
                            res.append('.'.join(segments))

    return res


'''
19216811
'''

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
