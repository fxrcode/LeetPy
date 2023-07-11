"""
Meta-cognition: Found it and thought it's close to Dec 18 Weekly contest Q4.
But it's not. Q4 should be len(subarr) - lis(subarr)
"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Greedy: https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/discuss/1163099/JavaPython-3-Straight-Forward-codes.
        """
        cnt = pre = 0
        for n in nums:
            if n <= pre:
                pre += 1
                cnt += pre - n
            else:
                pre = n
        # loop invariant: pre is modified cur n
        return cnt
