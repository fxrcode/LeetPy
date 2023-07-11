"""
✅ GOOD BFS

https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1388/
Leetcode explore Queue & Stack: Conclusion
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

XXX: tip 1: Q: how to calculate the distance of 2 cells? Ans: abs(r1-r2) + abs(c1-c2)
XXX: tip 2: Q: how to use BFS to calculate sssp from 1 to 0? Ans: rather bfs from 1 to reach 0 which make lavel 1's step = 0, then 1.
            We can reverse the bfs's source/destination by bfs from 0 to 1, then level 1 = 0, level 2 = 1!
"""


from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Only you know how to solve this problem then you understand BFS.
        Ref:
        1. nice and clean diagram to understand https://leetcode.com/problems/01-matrix/discuss/363902/BFS-python-explained-and-commneted-(two-approaches)
        Similar problem: 1162. As Far from Land as Possible
        2. clear comment to fully understand https://leetcode.com/problems/01-matrix/discuss/1369741/C%2B%2BJavaPython-BFS-DP-solutions-with-Picture-Clean-and-Concise-O(1)-Space
        Your runtime beats 43.83 % of python3 submissions.

        """
        R, C = len(mat), len(mat[0])
        q = deque()
        visited = set()
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0:
                    # XXX: init queue with all 0's, similar as topo-sort to init with all 0-indegree nodes
                    q.append((i, j))
                    visited.add((i, j))
        # XXX: similar idea as topo-sort: init q with all sea cells (level 0)
        step = 1
        DIR = [0, 1, 0, -1, 0]
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for i in range(4):
                    xx, yy = x + DIR[i], y + DIR[i + 1]
                    if (0 <= xx < R and 0 <= yy < C) and (xx, yy) not in visited:
                        visited.add((xx, yy))
                        q.append((xx, yy))
                        mat[xx][yy] = step
            step += 1
        return mat

        """
        ans = [[0 for _ in range(C)] for _ in range(R)]

        def neigbhors(r, c):
            ret = []
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                xx, yy = r+dx, c+dy
                if not (0 <= xx < R and 0 <= yy < C):
                    continue
                ret.add((xx, yy))

        BUG: 1st thought, but not working, because distance is reversed... 1st layer of 1's dist = 0, but should not!
        def bfs(r, c) -> None:
            # level order traverse from 1, if found 0 update
            q = deque([(r, c)])
            step = 0
            while q:
                qlen = len(q)
                for _ in range(qlen):
                    r, c = q.popleft()
                    visited.add((r, c))

                    for x, y in neigbhors(r, c):
                        if mat[x][y] == 1 and (x, y) not in visited:
                            q.add((x, y))
                            ans[x][y] = step
                        if mat[x][y] == 0:
                            return
                step += 1

        for r in range(R):
            for c in range(C):
                if mat[r][c] == 0:
                    continue
                bfs(r, c)
        """


sl = Solution()
mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(sl.updateMatrix(mat))
mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
print(sl.updateMatrix(mat))
