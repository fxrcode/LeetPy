"""
tag: easy, math
Lookback:
- counting problem
"""

from collections import Counter
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        def fxr():
            # Runtime: 493 ms, faster than 9.16% of Python3 online submissions for Number of Equivalent Domino Pairs.
            pick2 = lambda x: x * (x - 1) // 2
            cnt = Counter()
            for domi in dominoes:
                domi.sort()
                cnt[tuple(domi)] += 1
            return sum(map(pick2, cnt.values()))

        return fxr()


sl = Solution()
assert sl.numEquivDominoPairs(dominoes=[[1, 2], [2, 1], [3, 4], [5, 6]]) == 1
assert sl.numEquivDominoPairs(dominoes=[[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]) == 3
assert sl.numEquivDominoPairs([[1, 1], [2, 2], [1, 1], [1, 2], [1, 2], [1, 1]]) == 4
