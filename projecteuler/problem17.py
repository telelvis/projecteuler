#!/usr/bin/python

"""
    Number letter counts
    Problem 17
    If the numbers 1 to 5 are written out in words: one, two, three, four, five,
     then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out
     in words, how many letters would be used?


    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 
    20 letters. The use of "and" when writing out numbers is in compliance with
     British usage.
"""

def number_to_words(n):
    d = {0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'}

    if n < 20:
        return d[n]
    elif n < 100:
        return d[n-n%10] + number_to_words(n%10)
    elif n < 1000:
        r = d[(n-n%100)/100] + 'hundred'
        if n%100 != 0:
            r += 'and' + number_to_words(n%100)
        return r
    elif n == 1000:
        return 'onethousand'
    else:
        raise Error('out of bounds')

s = 0
for i in range (1, 1001):
    s += len(number_to_words(i))

print s
