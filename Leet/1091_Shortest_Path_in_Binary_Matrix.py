"""
Tag: Medium, BFS
Lookback:
- common trick in DFS/BFS in grid: in-place update to 1 to indicate visited, rather extra vis set.
- given start & end, we can do bi-directional BFS to speed up.

https://leetcode.com/explore/learn/card/graph/620/breadth-first-search-in-graph/3896/
Leetcode Explore Graph: BFS
"""


from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def fxr():
            """
            Runtime: 754 ms, faster than 63.45% of Python3 online submissions for Shortest Path in Binary Matrix.

            T: O(N) since each node is visited once at most
            M: O(N) for the visited set
            """
            DIR = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
            R, C = len(grid), len(grid[0])

            src, dst = (0, 0), (R - 1, C - 1)
            q = deque([src])
            if grid[0][0] == 1:
                return -1
            grid[0][0] = 1
            step = 1
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    # process cur
                    if (i, j) == dst:
                        return step
                    for dx, dy in DIR:
                        x, y = i + dx, j + dy
                        if not (0 <= x < R and 0 <= y < C and grid[x][y] == 0):
                            continue
                        grid[x][y] = 1
                        q.append((x, y))
                step += 1
            return -1

        return fxr()


sl = Solution()
print(sl.shortestPathBinaryMatrix(grid=[[0, 1], [1, 0]]))
print(sl.shortestPathBinaryMatrix(grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
print(sl.shortestPathBinaryMatrix(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
