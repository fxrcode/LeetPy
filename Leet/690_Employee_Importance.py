"""
tag: medium, dfs, hash
Lookback:
- consider DSA as cache. We need to fast get employee by id, so build a map for it
"""

from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        def fxr():
            """
            Runtime: 160 ms, faster than 88.52% of Python3 online submissions for Employee Importance.
            """
            mp = {e.id: e for e in employees}

            def dfs(id):
                e = mp[id]
                tot = e.importance
                for sub in e.subordinates:
                    tot += dfs(sub)
                return tot

            return dfs(id)
