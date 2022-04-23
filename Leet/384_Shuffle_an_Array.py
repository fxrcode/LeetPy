"""
tag: Medium, Google
Lookback:
- Fisher-Yates Algorithm: in-place swap
- If we put each number in a "hat" and draw them out at random, the order in which we draw them will define a random ordering.

"""

from random import randrange
from typing import List


class Solution:
    """
    Runtime: 368 ms, faster than 54.83% of Python3 online submissions for Shuffle an Array.

    T: O(N)
    """

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.ori = list(nums)

    def reset(self) -> List[int]:
        self.arr = self.ori
        self.ori = list(self.ori)
        return self.arr

    def shuffle(self) -> List[int]:
        def swap(A, i, j):
            A[i], A[j] = A[j], A[i]

        for i in range(len(self.arr)):
            swap_idx = randrange(i, len(self.arr))
            swap(self.arr, swap_idx, i)
        return self.arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
