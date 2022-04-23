'''
https://leetcode.com/explore/learn/card/graph/620/breadth-first-search-in-graph/3896/
Leetcode Explore Graph: BFS

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

The length of a clear path is the number of visited cells of this path.
'''


from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Your runtime beats 51.57 % of python3 submissions.

        T: O(N) since each node is visited once at most
        M: O(N) for the visited set
        AC in 1st.
        """
        DIR = [(-1, 0), (-1, 1), (0, 1), (1, 1),
               (1, 0), (1, -1), (0, -1), (-1, -1)]

        if not grid or grid[0][0] != 0:
            return -1

        R, C = len(grid), len(grid[0])

        source, target = (0, 0), (R-1, C-1)
        q = deque([source])
        visited = set([source])
        step = 1
        while q:
            qlen = len(q)
            for _ in range(qlen):
                x, y = q.popleft()
                # process cur
                if (x, y) == target:
                    return step
                for dx, dy in DIR:
                    xx, yy = x+dx, y+dy
                    if not (0 <= xx < R and 0 <= yy < C and grid[xx][yy] == 0 and (xx, yy) not in visited):
                        continue
                    q.append((xx, yy))
                    visited.add((xx, yy))
            step += 1
        return -1


sl = Solution()
print(sl.shortestPathBinaryMatrix(grid=[[0, 1], [1, 0]]))
print(sl.shortestPathBinaryMatrix(grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
print(sl.shortestPathBinaryMatrix(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
