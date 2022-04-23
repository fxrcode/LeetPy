"""
Daily Challenge (Mar 28, 2022)
tag: medium, bisect
Lookback:
- use Hoare partition to dedup!
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def fxr():
            """
            Runtime: 98 ms, faster than 19.42% of Python3 online submissions for Search in Rotated Sorted Array II.

            XXX: after WA, RE, WA debug
            """
            l, r = 0, len(nums) - 1
            while l < r:
                # similar to Hoare partition or #15: 3 Sum
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                if l == r:
                    return nums[l] == target
                mid = (l + r) // 2
                if nums[mid] == target:
                    return True
                if nums[mid] >= nums[l]:
                    if nums[l] <= target <= nums[mid]:
                        r = mid
                    else:
                        l = mid + 1
                else:
                    if nums[mid] <= target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid
            return nums[l] == target

        return fxr()


sl = Solution()
print(sl.search([1, 0, 1, 1, 1], 0))
print(sl.search([1, 1], 0))
print(sl.search([1, 3, 5], 1))
print(sl.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))
print(sl.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3))
