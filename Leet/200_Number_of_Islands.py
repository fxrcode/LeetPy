"""
✅ GOOD DFS (CC)
Tag: Medium, DFS
Lookback:
- This dfs is foundation of 694
- hiepit dfs return 0/1, sounds like 463

Similar:
- 694. Number of Distinct Islands (DFS Path Signature)
https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1380/
Leetcode Explore-Queue-Stack
"""
from typing import List


class Solution:
    def numIslands_leet_explore(self, grid: List[List[str]]) -> int:
        DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def hiepit_dfs():
            """
            Runtime: 483 ms, faster than 30.66% of Python3 online submissions for Number of Islands.
            T/M: O(MN)

            XXX: nice DFS CC w/ return 0/1
            """
            m, n = len(grid), len(grid[0])

            def dfs(i, j):
                if not (0 <= i < m and 0 <= j < n) or grid[i][j] == "0":
                    return 0
                grid[i][j] = "0"
                for dx, dy in DIR:
                    dfs(i + dx, j + dy)
                return 1

            cc = 0
            for i in range(m):
                for j in range(n):
                    cc += dfs(i, j)
            return cc

        return hiepit_dfs()


sl = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(sl.numIslands_leet_explore(grid))
