#!/usr/bin/python

"""
    Summation of primes
    Problem 10
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
"""

#from problem3 import is_prime

#print sum([i for i in range(3,2000000,2) if is_prime(i)]) + 2

"""
    Sieve of Eratosphenes
"""

n = 2000000
primes = set(range(2,n))

for i in list(primes):
    if i in primes:
        primes -= set(range(i+i, n ,i))

print sum(primes)
