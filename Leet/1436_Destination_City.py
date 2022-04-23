"""
tag: Easy, Hash
Lookback:
"""

from collections import Counter
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        def fxr():
            # Runtime: 71 ms, faster than 58.06% of Python3 online submissions for Destination City.
            DEG = Counter()
            for s, d in paths:
                DEG[s] += 1
                DEG[d] += 0
            for c in DEG:
                if DEG[c] == 0:
                    return c

        return fxr()


sl = Solution()
print(sl.destCity(paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
print(sl.destCity(paths=[["B", "C"], ["D", "B"], ["C", "A"]]))
