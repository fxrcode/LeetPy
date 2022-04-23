"""

✅ GOOD Bisect!
https://leetcode.com/explore/learn/card/binary-search/126/template-ii/948/
Leetcode Explore: Binary Search - Template II
tag: bisect, logic 
similar:
- 
"""
from typing import List

INF = 1e10


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Your runtime beats 58.15 % of python3 submissions.

        XXX: logic, logic, logic! Don't translate word by word of problem. Implement according to logic!
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # XXX: No need to use exact condition as stated in origin problem
            # if nums[mid-1] > nums[mid] > nums[mid+1]:
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l

    def findPeakElement_recur(self, nums: List[int]) -> int:
        """
        XXX: Because peak divided araay into 2 sorted array! We can do recursive binary search!
        This is approach 2 in official solutions
        """

        def bs(l, r):
            if l == r:
                return l
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                return bs(l, mid)
            else:
                return bs(mid + 1, r)

        return bs(0, len(nums) - 1)


sl = Solution()
print(sl.findPeakElement(nums=[1, 2, 3, 1]))
print(sl.findPeakElement(nums=[1, 2, 1, 3, 5, 6, 4]))
print(sl.findPeakElement_recur(nums=[5]))
