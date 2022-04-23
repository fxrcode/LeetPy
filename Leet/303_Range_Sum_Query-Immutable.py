"""
TuSimple List

Meta: classic prefix-sum
"""

from typing import List


class NumArray:
    """
    Runtime: 76 ms, faster than 83.83% of Python3 online submissions for Range Sum Query - Immutable.

    """

    def __init__(self, nums: List[int]):
        # P[i] = sum(...i-1)
        self.P = [0] * (len(nums) + 1)
        for i in range(1, len(self.P)):
            self.P[i] = self.P[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        # sum(i...j) = sum(...j) - sum(...i-1)
        return self.P[right + 1] - self.P[left]
