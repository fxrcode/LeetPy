'''
Google tag
tag: Easy
'''

from collections import Counter
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        def fxr():
            """
            Runtime: 32 ms, faster than 86.73% of Python3 online submissions for Number of Good Pairs.

            T: O(N)
            AC in 1
            """
            C = Counter(nums)
            f = lambda x: x * (x - 1) // 2
            return sum(f(v) for v in C.values())