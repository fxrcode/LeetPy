"""
Tag: Medium, DFS
Lookback:
- classic DFS
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def fxr():
            """
            Runtime: 182 ms, faster than 70.73% of Python3 online submissions for Max Area of Island.
            T: O(RC)
            """
            best = 0
            DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            R, C = len(grid), len(grid[0])

            def area(i, j):
                if not ((0 <= i < R) and (0 <= j < C) and grid[i][j] == 1):
                    return 0
                grid[i][j] = 0
                ans = 1
                for dx, dy in DIR:
                    r, c = i + dx, j + dy
                    ans += area(r, c)
                return ans

            for i in range(R):
                for j in range(C):
                    best = max(best, area(i, j))
            return best

        return fxr()


sl = Solution()
grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
print(sl.maxAreaOfIsland(grid))
