"""
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
Day 10: DP on String
"""


from collections import defaultdict
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        def fxr_lis():
            """
            Runtime: 2756 ms, faster than 13.26% of Python3 online submissions for Maximum Length of Pair Chain.

            T: O(N^2)
            """
            pairs.sort(key=lambda pa: (pa[0], pa[1]))
            T, m = defaultdict(lambda: 1), len(pairs)
            T[0] = 1
            for i in range(1, m):
                for j in range(i):
                    if pairs[j][1] < pairs[i][0]:
                        T[i] = max(T[i], T[j] + 1)
            return max(T.values)
