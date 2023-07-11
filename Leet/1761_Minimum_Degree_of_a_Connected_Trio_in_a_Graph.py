"""
TuSimple list
"""

from collections import defaultdict
from typing import List


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        def fxr():
            """
            Runtime: 813 ms, faster than 86.74% of Python3 online submissions for Minimum Degree of a Connected Trio in a Graph.

            REF: https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/discuss/1204311/Python-Sorting-degree-with-explanation-details
            T: O(V^3)
            M: O(E)
            """
            AL = {i: set() for i in range(1, n + 1)}

            for u, v in edges:
                AL[u].add(v)
                AL[v].add(u)

            mn = 1e6
            for u in sorted(range(1, n + 1), key=lambda x: len(AL[x])):
                # BUG: if len(AL[u]) >= mn//3
                if len(AL[u]) * 3 >= mn:
                    break
                for v in AL[u]:
                    for o in AL[u].intersection(AL[v]):
                        # for w in AL[v]:
                        #     if w in AL[u]:
                        deg = len(AL[u]) + len(AL[v]) + len(AL[o])
                        mn = min(deg, mn)
            if mn == 1e6:
                return -1
            return mn - 6

        return fxr()


sl = Solution()
print(
    sl.minTrioDegree(
        13,
        [
            [12, 4],
            [12, 1],
            [3, 4],
            [4, 6],
            [12, 13],
            [3, 10],
            [9, 5],
            [5, 10],
            [8, 9],
            [10, 6],
            [13, 2],
            [2, 11],
            [13, 5],
            [13, 11],
            [10, 12],
            [7, 4],
            [6, 11],
            [7, 10],
            [6, 8],
            [4, 5],
            [5, 6],
            [3, 12],
            [8, 2],
            [9, 1],
            [11, 4],
            [8, 11],
            [9, 4],
            [10, 2],
            [11, 7],
            [2, 4],
            [13, 4],
            [9, 13],
            [9, 10],
            [2, 7],
            [10, 8],
            [13, 7],
            [1, 2],
            [7, 3],
            [7, 9],
            [6, 7],
            [6, 13],
            [7, 12],
            [12, 5],
            [12, 11],
            [12, 8],
            [3, 5],
            [3, 11],
            [5, 2],
            [4, 10],
            [3, 8],
            [9, 6],
            [9, 12],
            [10, 1],
            [1, 4],
            [8, 13],
            [1, 7],
            [1, 13],
            [2, 6],
            [7, 5],
            [6, 3],
        ],
    )
)
