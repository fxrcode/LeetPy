"""
https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/
Leetcode Explore: Array 101. Delete from Array
https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1173/
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
"""


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Runtime: 80 ms, faster than 93.23% of Python3 online submissions for Remove Duplicates from Sorted Array.
        AC in 1st try. Now I have clear loop-invariant before coding.
        """
        if not nums:
            return 0
        s = 0
        for f in range(len(nums)):
            # loop-invariant: [0:s] has no duplicates
            if nums[f] != nums[s]:
                s += 1
                nums[s] = nums[f]
        return s + 1


sl = Solution()
print(sl.removeDuplicates([1, 1, 2]))
