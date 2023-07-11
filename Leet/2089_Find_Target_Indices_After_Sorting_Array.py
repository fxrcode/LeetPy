"""
Weekly Contest 269 (Nov 27, 2021)
"""

from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        begin = bisect_left(nums, target)
        if begin == len(nums) or nums[begin] != target:
            return []
        return range(begin, bisect_right(nums, target))


sl = Solution()
print(sl.targetIndices([1], 2))
