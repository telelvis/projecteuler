#!/usr/bin/python
# coding: utf-8

"""
    Amicable numbers
    Problem 21
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
"""

from problem12 import get_divisors

amis = {i: sum([j for j in get_divisors(i) if i!=j]) for i in range(1, 10000)}
s = 0
simi = {}

for i,k in amis.items():
    if not simi.has_key(k):
        simi[k] = []
    while k in amis.values():
        simi[k].append(amis.keys()[amis.values().index(k)])
        amis.pop(i)

print simi