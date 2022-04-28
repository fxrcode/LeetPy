"""
Tag: Easy, Array
Lookback:
- same as #1991
Explore Array & String
https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/
"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Runtime: 189 ms, faster than 58.41% of Python3 online submissions for Find Pivot Index.
        XXX: didn't bug free in 1st, careful in coding basics, loop-invariant.
        """
        left = 0
        tot = sum(nums)
        for i, n in enumerate(nums):
            right = tot - n - left
            if left == right:
                return i
            left += nums[i]
        return -1


sl = Solution()
print(sl.pivotIndex(nums=[1, 7, 3, 6, 5, 6]))
print(sl.pivotIndex([1, 2, 3]))
print(sl.pivotIndex([2, 1, -1]))
