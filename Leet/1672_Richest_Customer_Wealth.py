"""
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

tag: easy
Lookback:
- pythonic 1-liner
"""


from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Runtime: 85 ms, faster than 39.43% of Python3 online submissions for Richest Customer Wealth.

        """
        return max(map(sum, accounts))
