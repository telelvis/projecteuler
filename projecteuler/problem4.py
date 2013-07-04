#!/usr/bin/python
"""
(c) projecteuler.net
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

for i in range(999, 900, -1):
    num = int(str(i)+ str(i)[::-1])
    for j in range(999, 900, -1):
        if num%j == 0 and num/j<1000:
            print num
            break
