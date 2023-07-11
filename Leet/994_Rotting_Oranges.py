"""
https://leetcode.com/explore/learn/card/graph/620/breadth-first-search-in-graph/3898/
Leetcode Explore Graph: BFS

tag: medium, bfs

Lookback:
- smartly use BFS template to be elegant!
- keyword: shortest => ring bell multi-source BFS

similar:
- 1162
- 847
"""

import collections
from itertools import product
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def steam23_bfs():
            """
            Runtime: 89 ms, faster than 30.91% of Python3 online submissions for Rotting Oranges.

            https://leetcode.com/problems/rotting-oranges/discuss/388104/Python-10-lines-BFS-beat-97

            XXX: Same code as 1162!
            """
            m, n = len(grid), len(grid[0])
            rotting = {
                (i, j) for i, j in product(range(m), range(n)) if grid[i][j] == 2
            }
            fresh = {(i, j) for i, j in product(range(m), range(n)) if grid[i][j] == 1}
            ts = 0
            while fresh:
                if not rotting:
                    return -1
                rotting = {
                    (i + di, j + dj)
                    for i, j in rotting
                    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    if (i + di, j + dj) in fresh
                }
                fresh -= rotting
                ts += 1
            return ts

        return steam23_bfs()

        def os_bfs():
            """
            Your runtime beats 57.40 % of python3 submissions.

            REF: OS. Framework/templates is for you to learn, learn to use it flexibly for each specific question!!!
            T: O(N^2), M: O(N^2)
            """
            R, C = len(grid), len(grid[0])
            visited = set()
            q = collections.deque()
            fresh_cnt = 0
            if not grid or len(grid) == 0:
                return 0
            # init q with all rot
            for x in range(R):
                for y in range(C):
                    if grid[x][y] == 2:
                        q.append((x, y))
                        visited.add((x, y))
                    elif grid[x][y] == 1:
                        fresh_cnt += 1

            DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            step = 0
            # XXX: BFS should stop ASAP all rotten! so we have correct min.
            while q and fresh_cnt > 0:
                qlen = len(q)
                for _ in range(qlen):
                    x, y = q.popleft()
                    # process cur here

                    for dx, dy in DIR:
                        xx, yy = x + dx, y + dy
                        if not (0 <= xx < R and 0 <= yy < C):
                            continue
                        if (xx, yy) in visited or grid[xx][yy] != 1:
                            continue
                        fresh_cnt -= 1
                        q.append((xx, yy))
                        visited.add((xx, yy))
                        grid[xx][yy] = 2
                step += 1

            # BUG: should check fresh_cnt during BFS so we can stop asap all rotten!
            # for x in range(R):
            #     for y in range(C):
            #         if grid[x][y] == 1:
            #             return -1

            return step if fresh_cnt == 0 else -1


sl = Solution()
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
print(sl.orangesRotting(grid))
