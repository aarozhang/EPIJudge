import string

from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    col_num = 0

    for i in range(len(col)):
        col_num = col_num * 26 + ord(col[i]) - ord('A') + 1

    return col_num


if __name__ == '__main__':
    # print(ss_decode_col_id('A'))
    # print(ss_decode_col_id('B'))
    # print(ss_decode_col_id('Y'))
    # print(ss_decode_col_id('Z'))
    # print(ss_decode_col_id('AA'))
    # print(ss_decode_col_id('AB'))
    # print(ss_decode_col_id('YZ'))
    # print(ss_decode_col_id('ZZ'))

    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
