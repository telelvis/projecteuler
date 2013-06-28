#!/usr/bin/python
"""
(c) projecteuler.net
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

"""
Slow brutecode =(
"""

def is_prime(n):
    i = 2
    m = int(n/i)
    while i <= m:
        if n%i == 0:
            return False
        i += 1
        m = int(n/i)
    return True


def largest_prime_factor(n):
    i = 1
    m = int(n/i)
    while 1:
        if n%m == 0 and is_prime(m):
            return m
        i += 1
        m = int(n/i)

print largest_prime_factor(600851475143)
