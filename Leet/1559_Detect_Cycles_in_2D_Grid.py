"""
✅ GOOD UF
✅ GOOD DFS
tag: medium, DFS, UF
Lookback
- DFS (seen set vs 3-color?)
    前者常用于无向图。后者用于有向图的cycle detection
- UF (only up+left): to prevent duplicate merge!
[ ] REDO
"""


from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def os_uf():
            """
            Runtime: 2201 ms, faster than 96.30% of Python3 online submissions for Detect Cycles in 2D Grid.

            UF is neat to detect cycle!
            """

            class UF:
                def __init__(self, n) -> None:
                    self.pa = list(range(n))
                    self.sz = [1] * n
                    self.cnt = n

                def find(self, i):
                    if self.pa[i] != i:
                        self.pa[i] = self.find(self.pa[i])
                    return self.pa[i]

                def union(self, x, y):
                    if x == y:
                        return
                    if self.sz[x] > self.sz[y]:
                        x, y = y, x
                    self.pa[x] = y
                    self.sz[y] += self.sz[x]
                    self.cnt -= 1

                def find_and_union(self, i, j):
                    # T: not connected, but cycle after union! F: already same group
                    x, y = map(self.find, [i, j])
                    if x == y:
                        return False
                    self.union(x, y)
                    return True

            m, n = len(grid), len(grid[0])
            uf = UF(m * n)
            for i in range(m):
                for j in range(n):
                    if i > 0 and grid[i][j] == grid[i - 1][j]:
                        if not uf.find_and_union((i * n + j), ((i - 1) * n + j)):
                            return True

                    if j > 0 and grid[i][j] == grid[i][j - 1]:
                        if not uf.find_and_union((i * n + j), (i * n + j - 1)):
                            return True
            return False

        def carloscerlira_dfs():
            """
            Runtime: 3703 ms, faster than 45.10% of Python3 online submissions for Detect Cycles in 2D Grid.

            https://leetcode.com/problems/detect-cycles-in-2d-grid/discuss/806236/Python-Simple-DFS
            """

            def dfs(v, fa):
                """
                # 1st time seen-dfs detect cycle in undirected graph
                similar: 687,
                """
                if v in seen:
                    return True
                seen.add(v)
                x, y = v
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    xx, yy = x + dx, y + dy
                    # !no back edge (u->v->w), so don't choose u === w.
                    if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == grid[x][y] and (xx, yy) != fa:
                        w = (xx, yy)
                        if dfs(w, v):  # early termination to speedup
                            return True
                return False

            seen = set()
            m, n = len(grid), len(grid[0])
            for i in range(m):
                for j in range(n):
                    if (i, j) in seen:
                        continue
                    if dfs((i, j), None):
                        return True
            return False

        # return carloscerlira()
        return os_uf()


sl = Solution()
# grid = [["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]
# grid = [["c", "c", "c", "a"], ["c", "d", "c", "c"], ["c", "c", "e", "c"], ["f", "c", "c", "c"]]
grid = [["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]
print(sl.containsCycle(grid))
