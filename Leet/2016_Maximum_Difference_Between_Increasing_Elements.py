"""
Tag: Easy
Lookback:
- disguise of 121. Best Time to Buy and Sell Stock
"""

from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        def votrubac():
            """
            The only difference from 121. Best Time to Buy and Sell Stock is that we need to return -1 if no profit can be made.

            """
            mn = nums[0]
            res = -1
            for i in range(1, len(nums)):
                res = max(res, nums[i] - mn)
                mn = min(mn, nums[i])
            return res if res else -1

        def fxr():
            """
            Runtime: 78 ms, faster than 41.25% of Python3 online submissions for Maximum Difference Between Increasing Elements.

            """
            mn = 2e9
            ans = 0
            for n in nums:
                mn = min(mn, n)
                ans = max(ans, n - mn)
            return ans if ans else -1
