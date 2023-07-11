"""
https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1176/
Leetcode Explore: Hash Table. Practical Application - HashSet
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

required: T: O(N), S: O(1)
"""


from typing import List


class Solution:
    def singleNumber_forum(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]

    def singleNumber(self, nums: List[int]) -> int:
        """
        Your runtime beats 86.02 % of python3 submissions.
        AC in 1st try
        """
        res = 0
        for n in nums:
            res ^= n
        return res
