"""
Tag: Easy, Sort
Lookback:
- Same as #274. H-index
"""

from bisect import bisect_left
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def lenchen1112_h_index():
            # TODO: [ ]  not understood
            nums.sort(reverse=True)
            i = 0
            while i < len(nums) and nums[i] > i:
                i += 1
            return -1 if i < len(nums) and nums[i] == i else i

        return lenchen1112_h_index()

        def fxr():
            """
            Runtime: 49 ms, faster than 48.71% of Python3 online submissions for Special Array With X Elements Greater Than or Equal X.
            T: O(nlogn)
            """
            nums.sort()
            if len(nums) < nums[0]:
                return len(nums)

            for x in range(nums[0], nums[-1] + 1):
                ge_x = len(nums) - bisect_left(nums, x)
                if ge_x == x:
                    return x
            return -1

        return fxr()


sl = Solution()
print(sl.specialArray([3, 6, 7, 7, 0]))
# print(sl.specialArray([3, 5]))
# print(sl.specialArray([0, 0]))
# print(sl.specialArray([0, 4, 3, 0, 4]))
