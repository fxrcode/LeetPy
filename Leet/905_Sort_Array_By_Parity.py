"""
Tag: Easy, 2ptr
Lookback:
- classic Hoare partition (l<=r)
- Lomuto invariant: [0...l] is even, [l+1...i] is odd
https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/
leetcode explore: Array 101. In-place operations
"""
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        def fxr_hoare():
            """
            Runtime: 89 ms, faster than 70.27% of Python3 online submissions for Sort Array By Parity.

            """
            l, r = 0, len(nums) - 1
            while l <= r:
                while l <= r and nums[l] % 2 == 0:
                    l += 1
                while l <= r and nums[r] % 2 != 0:
                    r -= 1
                if l <= r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l, r = l + 1, r - 1
            return nums

        return fxr_hoare()

        def fxr_lomuto():
            """
            Your runtime beats 68.24 % of python3 submissions.
            AC in 1st try.
            XXX: Lomuto partition: init s; swap

            """
            l = -1
            for i in range(len(nums)):
                if nums[i] % 2 == 0:
                    l += 1
                    nums[l], nums[i] = nums[i], nums[l]
            return nums


sl = Solution()
print(sl.sortArrayByParity([3, 1, 2, 4]))
print(sl.sortArrayByParity([0]))
