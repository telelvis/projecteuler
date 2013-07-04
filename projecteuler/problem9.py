#!/usr/bin/python
"""
    (c) projecteuler.net
    Special Pythagorean triplet
    Problem 9
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for 
    which,

    a**2 + b**2 = c**2
    For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
"""

"""
    Equations:
    a*a + b*b = c*c
    a + b + c = 1000
    =>
    a*a + b*b = (1000 - a - b )**2
    =>
    b = (1000**2 - 2000*a)/(2000 - 2*a)
"""

for a in range(1, 1000):
    b = (1000**2 - 2000*a)/(2000 - 2*a)
    c = (a*a + b*b)**0.5
    if c > b > a and a+b+c == 1000:
        print a*b*c
        break
