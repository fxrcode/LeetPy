"""
https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3912/
Leetcode Explore Graph: Disjoint Set Union (DSU)

There are n people in a social group labeled from 0 to n - 1. You are given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.

Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.
Tag: medium, UF
"""

from typing import List


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        def fxr_dsu():
            """
            Runtime: 100 ms, faster than 99.06% of Python3 online submissions for The Earliest Moment When Everyone Become Friends.

            AC in 2nd. Forgot to sort logs by timestamp!
            T: O(E*logE) due to sort, M: O(V)
            """
            logs.sort(key=lambda tu: tu[0])
            fa = {i: i for i in range(n)}
            groups = n

            def find(x) -> int:
                if x != fa[x]:
                    fa[x] = find(fa[x])
                return fa[x]

            for ts, x, y in logs:
                rx, ry = find(x), find(y)
                if rx != ry:
                    fa[ry] = rx
                    groups -= 1
                    if groups == 1:
                        return ts
            return -1

        return fxr_dsu()
