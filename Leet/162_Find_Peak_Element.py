"""
✅ GOOD Bisect!
Tag: Bisect, logic
Lookback:
- Leetcode Explore: Binary Search - Template II
similar:
-
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def os_iter():
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

        return os_iter()

        def os_recur():
            """
            XXX: Because peak divided array into 2 sorted array! We can do recursive binary search!
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
print(sl.findPeakElement(nums=[5]))
