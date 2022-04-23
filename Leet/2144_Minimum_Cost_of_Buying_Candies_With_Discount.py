"""
tag: easy, sort
Lookback:

"""

from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        def fxr():
            # Runtime: 46 ms, faster than 86.52% of Python3 online submissions for Minimum Cost of Buying Candies With Discount.
            cost.sort(reverse=True)
            return sum(c for i, c in enumerate(cost) if (i + 1) % 3)

        return fxr()


sl = Solution()
print(sl.minimumCost(cost=[1, 2, 3]))
