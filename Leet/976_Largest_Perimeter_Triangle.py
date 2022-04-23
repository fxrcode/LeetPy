"""
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

tag: easy, math
Lookback:
- Do analysis before try!
Similar:
- 812
"""

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def os():
            """
            Runtime: 230 ms, faster than 68.40% of Python3 online submissions for Largest Perimeter Triangle.
            T: O(nlogn)
            """
            nums.sort()
            for i in range(len(nums) - 3, -1, -1):
                if nums[i] + nums[i + 1] > nums[i + 2]:
                    return nums[i] + nums[i + 1] + nums[i + 2]
            return 0

        return os()


sl = Solution()
print(sl.largestPerimeter(nums=[2, 6, 2, 5, 4, 15, 1]))
