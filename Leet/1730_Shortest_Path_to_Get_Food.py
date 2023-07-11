"""
Amazon Top50
tag: medium, BFS

Lookback: careful on TLE for some case.
"""

from collections import deque
from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        def fxr_bfs():
            """
            Runtime: 604 ms, faster than 49.28% of Python3 online submissions for Shortest Path to Get Food.
            T: O(MN)
            """
            m, n = len(grid), len(grid[0])
            foods = []
            steps = 0
            # TLE: 77 / 85 test cases passed. If mark X as visited, rather using visited set
            visited = set()

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == "#":
                        foods.append((i, j))
                        visited.add((i, j))

            q = deque(foods)

            while q:
                qlen = len(q)
                for _ in range(qlen):
                    x, y = q.popleft()

                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        xx, yy = x + dx, y + dy
                        if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in visited:
                            if grid[xx][yy] == "*":
                                return steps + 1
                            elif grid[xx][yy] == "O":
                                q.append((xx, yy))
                                visited.add((xx, yy))
                steps += 1
            return -1

        return fxr_bfs()


sl = Solution()
# grid = [["X", "X", "X", "X", "X", "X"], ["X", "*", "O", "O", "O", "X"],
#         ["X", "O", "O", "#", "O", "X"], ["X", "X", "X", "X", "X", "X"]]
# grid = [["X", "X", "X", "X", "X"], ["X", "*", "X", "O", "X"],
#         ["X", "O", "X", "#", "X"], ["X", "X", "X", "X", "X"]]
grid = [
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "*", "O", "X", "O", "#", "O", "X"],
    ["X", "O", "O", "X", "O", "O", "X", "X"],
    ["X", "O", "O", "O", "O", "#", "O", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X"],
]
print(sl.getFood(grid))
