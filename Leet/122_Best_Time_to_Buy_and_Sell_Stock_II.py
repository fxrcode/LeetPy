'''
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming
'''


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def fxr():
            """
            Runtime: 60 ms, faster than 83.68% of Python3 online submissions for Best Time to Buy and Sell Stock II.

            AC in 1.
            """
            ans = 0
            stock = prices[0]
            for i, p in enumerate(prices, start=1):
                if p < stock:
                    stock = p
                    continue
                ans += p-stock
                stock = p
            return ans

        return fxr()


sl = Solution()
print(sl.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(sl.maxProfit(prices=[1, 2, 3, 4, 5]))
