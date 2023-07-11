"""
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1154/
Explore Array & String: 2 pointer technique
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
"""
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        """
        Runtime: 252 ms, faster than 96.10% of Python3 online submissions for Array Partition I.
        AC in 1. <The Art and Craft of Problem Solving (3/e)>


        awice: Proof: Consider the smallest element x. It should be paired with the next smallest element, because min(x, anything) = x, and having bigger elements only helps you have a larger score. Thus, we should pair adjacent elements together in the sorted array.
        """
        nums.sort()
        ans = 0
        i = 0
        while i < len(nums):
            ans += nums[i]
            i += 2
        return ans


sl = Solution()
# nums = [1, 4, 3, 2]
nums = [6, 2, 6, 5, 1, 2]
print(sl.arrayPairSum(nums))
