"""
✅ GOOD Sort (cyclic-sort)
tag: easy, sort
Lookback:
- Coding Patterns: Cyclic Sort
Similar:
- 41
- 1528
- 1920
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def cyclic_sort():
            """
            Runtime: 195 ms, faster than 53.41% of Python3 online submissions for Missing Number.

            https://emre.me/coding-patterns/cyclic-sort/
            nice visualization
            """
            n = len(nums)
            i = 0

            while i < n:
                x = nums[i]
                if x < n and x != i:
                    nums[i], nums[x] = nums[x], nums[i]
                else:
                    i += 1

            for i, x in enumerate(nums):
                if x != i:
                    return i
            return n
