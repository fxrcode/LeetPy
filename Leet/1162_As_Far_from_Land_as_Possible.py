"""
tag: medium
similar: 
- 994 . Rotting Oranges
Lookback:
- multi-source BF
"""

from collections import deque
from itertools import product
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        def leihao1313_rotting_oranges():
            """
            similar to #994 . Rotting Oranges

            https://leetcode.com/problems/as-far-from-land-as-possible/discuss/360960/Python-BFS/822409

            """
            n, res = len(grid), 0
            land = {(i, j) for i, j in product(range(n), range(n)) if grid[i][j]}
            water = {(i, j) for i, j in product(range(n), range(n)) if not grid[i][j]}
            while water:
                if not land:
                    return -1
                land = {
                    (x, y)
                    for i, j in land
                    for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1))
                    if (x, y) in water
                }
                water -= land
                res += 1
            return res or -1

        return leihao1313_rotting_oranges()

        def os():
            """
            Runtime: 664 ms, faster than 77.61% of Python3 online submissions for As Far from Land as Possible.

            """
            m, n = len(grid), len(grid[0])
            q = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1])
            if len(q) == m * n:
                return -1
            seen = set(q)
            step = 0
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        xx, yy = x + dx, y + dy
                        if (
                            0 <= xx < m
                            and 0 <= yy < n
                            and grid[xx][yy] == 0
                            and (xx, yy) not in seen
                        ):
                            q.append((xx, yy))
                            seen.add((xx, yy))
                step += 1

            return step - 1


sl = Solution()
# grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
# grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
print(sl.maxDistance(grid))
