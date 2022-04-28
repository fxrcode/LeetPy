"""
Tag: Easy, Sort, BFS, DFS
Lookback:
- Good easy problem that can be solved in diff DSA
[ ] REDO
"""

from collections import deque
from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        def cenkay_dfs():
            """
            Runtime: 415 ms, faster than 5.67% of Python3 online submissions for Matrix Cells in Distance Order.

            """

            def dfs(i, j):
                vis.add((i, j))
                res.append((i, j))
                for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    if 0 <= x < rows and 0 <= y < cols and (x, y) not in vis:
                        dfs(x, y)

            res, vis = [], set()
            dfs(rCenter, cCenter)
            res.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
            return res

        return cenkay_dfs()

        def cenkay_bfs():
            """
            Runtime: 230 ms, faster than 44.58% of Python3 online submissions for Matrix Cells in Distance Order.

            """
            q, res = deque([(rCenter, cCenter)]), []
            vis = set(q)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    res.append((r, c))
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        xx, yy = r + dx, c + dy
                        if 0 <= xx < rows and 0 <= yy < cols and (xx, yy) not in vis:
                            vis.add((xx, yy))
                            q.append((xx, yy))
            return res

        return cenkay_bfs()

        def sunnyvaleCA():
            # Runtime: 156 ms, faster than 97.54% of Python3 online submissions for Matrix Cells in Distance Order.
            res = [(r, c) for r in range(rows) for c in range(cols)]
            res.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
            return res

        return sunnyvaleCA()

        def fxr():
            """
            Runtime: 420 ms, faster than 5.17% of Python3 online submissions for Matrix Cells in Distance Order.

            """
            res = set()
            for d in range(rows - 1 + cols - 1 + 1):
                for dx in range(d + 1):
                    dy = d - dx
                    for sx, sy in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                        nx, ny = rCenter + sx * dx, cCenter + sy * dy
                        if 0 <= nx < rows and 0 <= ny < cols:
                            res.add((nx, ny))
            sres = list(res)
            sres.sort(key=lambda x: (abs(x[0] - rCenter) + abs(x[1] - cCenter)))
            return sres

        return fxr()


sl = Solution()
print(sl.allCellsDistOrder(rows=1, cols=2, rCenter=0, cCenter=0))
print(sl.allCellsDistOrder(rows=2, cols=2, rCenter=0, cCenter=1))
print(sl.allCellsDistOrder(rows=2, cols=3, rCenter=1, cCenter=2))
