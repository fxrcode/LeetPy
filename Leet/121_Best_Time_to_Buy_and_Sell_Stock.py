"""
date: 02252023
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming II
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def fxr():
            """
            Runtime: 1476 ms, faster than 14.87% of Python3 online submissions for Best Time to Buy and Sell Stock.

            AC in 1.
            XXX: same idea as 1014. Best Sightseeing Pair
            """
            buy = prices[0]
            ans = 0
            for i in range(1, len(prices)):
                ans = max(ans, prices[i] - buy)
                buy = min(buy, prices[i])
            return ans

        return fxr()


sl = Solution()
print(sl.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(sl.maxProfit(prices=[7, 6, 4, 3, 1]))
