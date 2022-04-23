"""
tag: Medium, D&C, sort
Lookback:
- foundation D&C (merge-sort vs quick-sort)
- prerequisite for 327, 315

https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2944/
Leetcode explore Recursion II: Divide and Conquer
"""

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Your runtime beats 52.33 % of python3 submissions.
        Much slower than builtin sort, I guess the builtin will choose the best sort based on input nums list.

        Basic coding template: merge sort
        """

        def merge(L: List[int], R: List[int]) -> List[int]:
            i, j = 0, 0
            res = []
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    res.append(L[i])
                    i += 1
                else:
                    res.append(R[j])
                    j += 1
            res.extend(L[i:])
            res.extend(R[j:])
            return res

        def merge_sort(nums: List[int]) -> List[int]:
            # if l == r:
            # because edge case nums can be empty or single element
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            sorted_l = merge_sort(nums[:mid])
            sorted_r = merge_sort(nums[mid:])
            return merge(sorted_l, sorted_r)

        return merge_sort(nums)

    def sortArray_builtin(self, nums: List[int]) -> List[int]:
        # Your runtime beats 96.68 % of python3 submissions.
        nums.sort()
        return nums


sl = Solution()
print(sl.sortArray(nums=[5, 2, 3, 1]))
