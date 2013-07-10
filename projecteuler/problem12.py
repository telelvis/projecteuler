#!/usr/bin/python

"""
    Highly divisible triangular number
    Problem 12
    The sequence of triangle numbers is generated by adding the natural numbers.
    So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The 
    first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

    1: 1
    3: 1,3
    6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred 
    divisors?
"""

def get_triangle():
    i = s = 0
    while 1:
        i += 1
        s += i
        yield s


def get_divisors(n):
    i = 1
    while i < n/i:
        if n%i == 0:
            yield i
            yield n//i
        i += 1
    else:
        if n%i == 0:
            yield i
        yield n


if __name__ == '__main__':
    m = 0

    for i in get_triangle():
        c = len([j for j in get_divisors(i)])
        if c > m:
            m = c
            if m > 500:
                break

    print i
