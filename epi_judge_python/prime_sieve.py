from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    if n <= 1:
        return []

    primes = [False, False] + [True] * (n - 1)
    res = []

    for i in range(2, n + 1):
        if primes[i]:
            res.append(i)

            for j in range(i * 2, n + 1, i):
                primes[j] = False

    return res

'''
n = 10
[f, f, t, t, f, t, f, t, f, f, f]
'''


if __name__ == '__main__':
    # print(generate_primes(10))
    # print(generate_primes(1))
    # print(generate_primes(50))

    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
