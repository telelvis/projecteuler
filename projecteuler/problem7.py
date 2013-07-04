#!/usr/bin/python
"""
(c) projecteuler.net
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that 
the 6th prime is 13.

What is the 10 001st prime number?
"""

from problem3 import is_prime

i = 2
k = 1
while k != 10001:
    i += 1
    if is_prime(i):
        k += 1

print i

