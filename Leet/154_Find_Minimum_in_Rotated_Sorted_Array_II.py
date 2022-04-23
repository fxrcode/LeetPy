'''
✅ GOOD Bisect
https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1031/
Leetcode Explore: Binary Search - Conclusion

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?

tag: Hard, bisect

Similar:
81. Search in Rotated Sorted Array II

'''

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Your runtime beats 51.08 % of python3 submissions.

        XXX: don't over-complicated in case analysis!
        T: O(logN) avg, O(N) worst
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mi = (l + r) // 2

            if nums[mi] > nums[r]:
                # search right
                l = mi + 1
            elif nums[mi] < nums[l]:
                # search left
                r = mi
            else:
                # nums[l] <= nums[mi] <= nums[r], can't decide which way,
                # then converatively shrink search space
                r -= 1

        print(l, r)
        return nums[l]


sl = Solution()
sl.findMin(nums=[2, 2, 2, 0, 1])
print('hello')
sl.findMin(nums=[2, 0, 1, 1, 3])
