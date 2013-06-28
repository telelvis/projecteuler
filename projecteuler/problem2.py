#!/usr/bin/python
"""
(c) projecteuler.net
Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two 
terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued terms.
"""
fib = [1,2]
s = 2
while 1:
    fib += [fib[-2]+fib[-1]]
    if fib[-1]>4000000:
        break

    if fib[-1]%2 == 0:
        s += fib[-1]

print s