from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

    def backtrack(i):
        if len(partial) == len(phone_number):
            result.append(''.join(partial))
            return

        for c in MAPPING[int(phone_number[i])]:
            partial.append(c)
            backtrack(i + 1)
            partial.pop()

    result = []
    partial = []
    backtrack(0)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
