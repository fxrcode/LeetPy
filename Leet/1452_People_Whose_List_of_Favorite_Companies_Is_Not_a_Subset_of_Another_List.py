"""
tag: medium
Lookback:
- be familiar with Python collections
"""

from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        def rock():
            """
            Runtime: 738 ms, faster than 68.54% of Python3 online submissions for People Whose List of Favorite Companies Is Not a Subset of Another List.

            """
            s = [set(fc) for fc in favoriteCompanies]
            res = []
            for i, s1 in enumerate(s):
                if all(not s1.issubset(s2) for j, s2 in enumerate(s) if i != j):
                    res.append(i)
            return res
