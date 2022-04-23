"""
tag: easy, logic
Lookback:
- draw it then the logic is clear
"""

from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        def fxr():
            # Runtime: 133 ms, faster than 71.52% of Python3 online submissions for Smallest Range I.
            mn, mx = min(nums), max(nums)
            return max(0, mx - mn - 2 * k)

        return fxr()


sl = Solution()
print(sl.smallestRangeI(nums=[1], k=0))
print(sl.smallestRangeI(nums=[0, 10], k=2))
print(sl.smallestRangeI(nums=[1, 3, 6], k=3))
print(sl.smallestRangeI([3, 1, 10], 4))
