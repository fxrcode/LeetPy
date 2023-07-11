"""
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
Day 6: 1D DP

[ ] REDO
"""


from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        def lee215():
            """
            Runtime: 680 ms, faster than 92.66% of Python3 online submissions for Toss Strange Coins.

            dp[c][k]: prob of tossing first c coints and get k faced up
            dp[c][k] = dp[c-1][k]*(1-p) + dp[c-1][k-1]*p
            """
            dp = [1] + [0] * target
            for p in prob:
                for k in range(target, -1, -1):
                    dp[k] = (dp[k - 1] if k else 0) * p + dp[k] * (1 - p)
            return dp[target]
