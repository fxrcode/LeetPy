"""
tag: easy, skills
Lookback:
- elegant logic (lee215)
"""

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def lee215():
            # Runtime: 1505 ms, faster than 34.96% of Python3 online submissions for Monotonic Array.
            inc = dec = True
            for i in range(1, len(nums)):
                inc &= nums[i - 1] <= nums[i]
                dec &= nums[i - 1] >= nums[i]
            return inc or dec

        return lee215()

        def fxr():
            # Runtime: 1671 ms, faster than 20.89% of Python3 online submissions for Monotonic Array.
            sign = lambda x: bool(x > 0) - bool(x < 0)
            sn = sign(nums[-1] - nums[0])
            for i in range(1, len(nums)):
                if sn == 0:
                    if not nums[i - 1] == nums[i]:
                        return False
                elif sn == 1:
                    if not nums[i - 1] <= nums[i]:
                        return False
                else:
                    if not nums[i - 1] >= nums[i]:
                        return False
            return True

        return fxr()


sl = Solution()
print(sl.isMonotonic(nums=[1, 2, 2, 3]))
print(sl.isMonotonic([6, 5, 4, 4]))
print(sl.isMonotonic(nums=[1, 3, 2]))
