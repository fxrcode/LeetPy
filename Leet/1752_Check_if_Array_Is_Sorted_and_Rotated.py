"""
💡✅ Logic
Tag: Easy, Logic
Lookback:
- Compare all neignbour elements (a,b) in A, the case of a > b can happen at most once.
- My simulate does AC but ugly & smell.
"""

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        def lee215():
            k, n = 0, len(nums)
            for i in range(n):
                if nums[i] > nums[(i + 1) % n]:
                    k += 1
                if k > 1:
                    return False
            return True

        return lee215()

        def fxr():
            """
            Runtime: 34 ms, faster than 87.80% of Python3 online submissions for Check if Array Is Sorted and Rotated.

            """
            mn = nums[0]
            for i in range(len(nums) - 1):
                if not nums[i] <= nums[i + 1]:
                    break
            else:
                return True
            for j in range(i + 1, len(nums)):
                if nums[j] > mn or j + 1 < len(nums) and nums[j] > nums[j + 1]:
                    return False
            return True

        return fxr()


sl = Solution()
print(sl.check(nums=[3, 4, 5, 1, 2]))
print(sl.check(nums=[2, 1, 3, 4]))
print(sl.check(nums=[1, 2, 3]))
