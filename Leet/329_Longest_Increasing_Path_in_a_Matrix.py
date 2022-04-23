"""
✅ GOOD DP (memo-dfs)
tag: Hard, DFS, DP
Lookback:
- classic 夜深人静写算法（二十六）- 记忆化搜索

https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
Day 15: Memoization
"""


from collections import defaultdict, deque
from functools import cache
from typing import List

DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    def longestIncreasingPath(self, M: List[List[int]]) -> int:
        def yerbola_toposort():
            """
            Runtime: 793 ms, faster than 23.58% of Python3 online submissions for Longest Increasing Path in a Matrix.

            Approach #3 (Peeling Onion) [Accepted]

            https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/402112/Python-Topological-Sorting-on-a-directed-graph
            T: O(V+E) === O(mn)
            """
            # step 1: build a DAG
            AL = defaultdict(list)
            IND = defaultdict(int)
            m, n = len(M), len(M[0])
            for i in range(m):
                for j in range(n):
                    neighbors = [(i + dx, j + dy) for dx, dy in DIR]
                    for x, y in neighbors:
                        if 0 <= x < m and 0 <= y < n and M[i][j] < M[x][y]:
                            AL[(i, j)].append((x, y))
                            IND[(x, y)] += 1
            # step 2: Topo-sort w/ Kahn's algs
            q = deque([(i, j) for i in range(m) for j in range(n) if (i, j) not in IND])
            mx_path_len = 0
            while q:
                mx_path_len += 1
                for _ in range(len(q)):
                    node = q.popleft()
                    for neigh in AL[node]:
                        IND[neigh] -= 1
                        if not IND[neigh]:
                            q.append(neigh)
            return mx_path_len

        return yerbola_toposort()

        def fxr_dfs_memo():
            """
            Approach #2 (DFS + Memoization)
            Runtime: 712 ms, faster than 17.98% of Python3 online submissions for Longest Increasing Path in a Matrix.

            T: O(MN)
            """
            m, n = len(M), len(M[0])

            @cache
            def dfs(i, j, pre):
                # base
                if not (0 <= i < m and 0 <= j < n) or M[i][j] <= pre:
                    return 0
                # recurrence
                res = 0
                for dx, dy in DIR:
                    xx, yy = i + dx, j + dy
                    res = max(res, 1 + dfs(xx, yy, M[i][j]))
                return res

            ans = 0
            for i in range(m):
                for j in range(n):
                    ans = max(ans, dfs(i, j, -1))
            return ans


sl = Solution()
print(sl.longestIncreasingPath(M=[[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
assert sl.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
