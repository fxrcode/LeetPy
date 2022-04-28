"""
Tag: Easy
Lookback:
- Count and check parity
"""

from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        def rock_alleven():
            return all(v % 2 == 0 for v in Counter(nums).values())

        def fxr():
            # Runtime: 89 ms, faster than 90.67% of Python3 online submissions for Divide Array Into Equal Pairs.
            nums.sort()
            for i in range(0, len(nums) - 1, 2):
                if nums[i] != nums[i + 1]:
                    return False
            return True
