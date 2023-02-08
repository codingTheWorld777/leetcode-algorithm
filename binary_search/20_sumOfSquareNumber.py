"""
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

***Example 1:***
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

***Example 2:***
Input: c = 3
Output: false
"""
import math

def judgeSquareSum(c):
    l, h = 0, int(math.sqrt(c))
    while l <= h:  # and l <= int(math.sqrt(c/2)) and h >= int(math.sqrt(c/2))
        if c - l ** 2 == h ** 2:
            return True
        elif c - l ** 2 > h ** 2:
            l += 1
        elif c - l ** 2 < h ** 2:
            h -= 1
    return False