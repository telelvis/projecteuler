#!/usr/bin/python
# coding: utf-8

"""
    Lattice paths
    Problem 15
    Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


    How many such routes are there through a 20×20 grid?
"""

"""
    I'm ashamed for this, I really do...
"""

total = 0

def spawn(x, y):
    global total
    if x+y != 40:
        if x < 20:
            spawn(x+1, y)
        if y < 20:
            spawn(x, y+1)
    else:
        total += 1

spawn(0, 0)
print total