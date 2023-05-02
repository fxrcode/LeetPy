"""
date: 04272023
Tag: Math, Easy
"""
from math import isqrt


class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        Runtime: 47 ms, faster than 17.63% of Python3 online submissions for Bulb Switcher.

        https://leetcode.com/problems/bulb-switcher/discuss/77104/Math-solution..
        """
        return isqrt(n)
