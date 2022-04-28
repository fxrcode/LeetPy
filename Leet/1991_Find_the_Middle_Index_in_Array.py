"""
Tag: Easy, Array
Lookback:
- clear on invariant, then it's easy
Note: This question is the same as 724: https://leetcode.com/problems/find-pivot-index/
"""

from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        def fxr():
            # Runtime: 48 ms, faster than 70.37% of Python3 online submissions for Find the Middle Index in Array.
            tot = sum(nums)
            left = 0
            for i, n in enumerate(nums):
                right = tot - n - left
                if left == right:
                    return i
                left += n
            return -1

        return fxr()


sl = Solution()
print(sl.findMiddleIndex(nums=[2, 3, -1, 8, 4]))
print(sl.findMiddleIndex(nums=[1, -1, 4]))
print(sl.findMiddleIndex(nums=[2, 5]))
