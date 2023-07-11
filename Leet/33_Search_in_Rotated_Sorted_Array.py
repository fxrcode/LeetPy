"""
tag: medium, bisect
Lookback:
- bisect in ordered segment, ow, 1-step move.
Similar:
- 81 (w/ duplicates)
https://leetcode.com/explore/learn/card/binary-search/125/template-i/952/
Leetcode Explore: Binary Search - Template I
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def os():
            """
            Runtime: 32 ms, faster than 98.50% of Python3 online submissions for Search in Rotated Sorted Array.

            XXX: The idea is that we add some additional condition checks in the normal binary search in order to better narrow down the scope of the search.

            T: O(logN)
            """
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] >= nums[l]:
                    if nums[l] <= target < nums[mid]:
                        r = mid
                    else:
                        l = mid + 1
                else:
                    if nums[mid] < target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid
            if nums[l] == target:
                return l
            return -1

        return os()

        def post_inf():
            """
            Your runtime beats 80.11 % of python3 submissions.

            REF: https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/154836/The-INF-and-INF-method-but-with-a-better-explanation-for-dummies-like-me

            XXX: how to solve non-easy Leetcode problem? Ans: transform (encoding) to common patterns!
                The skill to be able to transform/encoding a new problem takes 500 leetcode practices.

            XXX: coding is logic, not necessaryly to really transform the whole nums!
            XXX: we only concern nums[mid] when comparing to target, so only transform nums[mid]'s value!

            nums = [12, 13, 14, 7, 8, 9, 10, 11]
            a. target = 14, then nums = [12,13,14,inf,inf,inf,inf]
            b. target = 8, then nums = [-inf,-inf,-inf, 7,8,9,10,11]
            Then do the normal binary search
            """
            INF = 1e6
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2

                # XXX: check if mid is same side of target?
                #       careful in >, <=. if both in left, must use `nums[0] <= target,nums[mid]`, since nums[0] is inclusive in left side!
                v_mid = None
                if (nums[0] > target and nums[0] > nums[mid]) or (
                    nums[0] <= target and nums[0] <= nums[mid]
                ):
                    v_mid = nums[mid]
                else:  # if not same side, encode to -INF for left, and INF for right
                    if target < nums[0]:
                        v_mid = -INF
                    else:
                        v_mid = INF

                # XXX: then do regular binary search
                if v_mid >= target:
                    r = mid
                else:
                    l = mid + 1
            if nums[l] == target:
                return l
            return -1


sl = Solution()
print(sl.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print(sl.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
print(sl.search(nums=[1, 3], target=3))
print(sl.search(nums=[5, 1, 3], target=5))
