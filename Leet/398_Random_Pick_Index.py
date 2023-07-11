"""
Reservior Sampling
"""

import random
from typing import List


class Solution:
    """
    Runtime: 284 ms, faster than 89.26% of Python3 online submissions for Random Pick Index.

    """

    def __init__(self, nums: List[int]):
        self.A = nums

    def pick(self, target: int) -> int:
        count = 0
        idx = 0
        for i, n in enumerate(self.A):
            if n == target:
                count += 1
                if random.random() < 1 / count:
                    idx = i
        return idx
