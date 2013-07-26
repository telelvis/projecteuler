#!/usr/bin/python

"""
    Counting Sundays
    Problem 19
    You are given the following information, but you may prefer to do some 
    research for yourself.
    
    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century
     unless it is divisible by 400.
    How many Sundays fell on the first of the month during the twentieth century
     (1 Jan 1901 to 31 Dec 2000)?
"""

def get_mday(year, month):
    if month in (4, 6, 9, 11):
        for i in range(0, 30):
            yield i+1
    elif month == 2:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    for i in range(0, 29):
                        yield i+1
                    return
                for i in range(0, 28):
                    yield i+1
                return
            for i in range(0, 29):
                yield i+1
            return
        for i in range(0, 28):
            yield i+1
    else:
        for i in range(0, 31):
            yield i+1


l = 0
total = 0
for i in range(1900, 2001):
   for j in range(1, 13):
       for m in get_mday(i, j):
          l += 1
          if l % 7 == 0 and m == 1 and i > 1900:
              total += 1

print total