'''
✅ GOOD Bisect
https://leetcode.com/explore/learn/card/binary-search/126/template-ii/949/
Leetcode Explore: Binary Search - Template II

Given the sorted rotated array nums of unique elements, return the minimum element of this array.
tag: medium, bisect
'''

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Runtime: 56 ms, faster than 44.06% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

        REF: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/158940/Beat-100%3A-Very-Simple-(Python)-Very-Detailed-Explanation
        The condition is simple: find minimum k, st nums[k] <= nums[r]!
        eg. 4,5,6,0,1 => F,F,F, T,T
        eg. 0,1,4,5,6 => T,T,T,T,T
        search 1st T

        T: O(logN)
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1
        print(nums[l])
        return nums[l]

    def findMin_fxr(self, nums: List[int]) -> int:
        """
        Your runtime beats 98.24 % of python3 submissions.

        AC in 1.
        """
        if nums[0] < nums[-1]:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
                continue
            if nums[mid] < nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        # print(nums[l])
        return nums[l]


sl = Solution()
sl.findMin(nums=[3, 4, 5, 1, 2])
sl.findMin(nums=[4, 5, 6, 7, 0, 1, 2])
sl.findMin(nums=[1])
