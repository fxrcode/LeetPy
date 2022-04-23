"""
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

tag: easy, skills
Lookback
- Brian Kernighan method: turn off rightmost set bit. 
"""

from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def fxr():
            """
            Runtime: 76 ms, faster than 82.43% of Python3 online submissions for Sort Integers by The Number of 1 Bits.

            """

            def bits(v):
                ones = 0
                while v:
                    ones += 1
                    v &= v - 1
                return ones

            arr.sort(key=lambda x: (bits(x), x))
            return arr
