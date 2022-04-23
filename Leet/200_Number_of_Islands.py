"""
https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1380/
Leetcode Explore-Queue-Stack
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""
from typing import List
from collections import deque


class Solution:
    def numIslands_leet_explore(self, grid: List[List[str]]) -> int:
        """[summary]
        Your runtime beats 18.79 % of python3 submissions.
        0917: explore queue & stack. I forgot DFS template...
        """
        def dfs(r, c) -> None:
            # action now
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            if grid[r][c] != '1':
                return
            # action on cur node
            grid[r][c] = '.'
            # recur
            for xx, yy in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                dfs(xx, yy)

        if not grid:
            return 0
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)  # flood-fill
        return islands
        """
        def dfs(r, c):
            BUG: wtf am I doing?!
            visited = set()
            for r in len(grid):
                for c in len(grid[0]):
                    if grid[r][c] == '1':
                        # mark all island '.' except this one for later count island numbers
        """

    def numIslands_DFS(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return
            if grid[i][j] != '1':
                return
            grid[i][j] = '.'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)

        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count

    def numIslands_BFS(self, grid: List[List[str]]) -> int:
        """[summary]
        Runtime: 372 ms, faster than 5.00% of Python3 online submissions for Number of Islands.
        """
        visited = {}
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '0':
                    continue
                if (r, c) in visited:
                    continue
                self.bfs(grid, r, c, visited)
                print((r, c))
                count += 1
        return count

    def bfs(self, grid, r, c, visited):
        def valid(grid, xx, yy) -> bool:
            R, C = len(grid), len(grid[0])
            return 0 <= xx < R and 0 <= yy < C and grid[xx][yy] == '1'

        q = deque([(r, c)])
        visited[(r, c)] = True

        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    xx, yy = x+dx, y+dy
                    if valid(grid, xx, yy) and (xx, yy) not in visited:
                        visited[(xx, yy)] = True
                        q.append((xx, yy))


sl = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(sl.numIslands_leet_explore(grid))
