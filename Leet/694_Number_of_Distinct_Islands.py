"""
✅ GOOD DFS (path signature)
Tag: Medium, DFS, Hash
Lookback:
- classic Grid Path Signature
- or use normalization + hash (frozenset)
    - this is easier to be extend to 711
- same as 711, we don't need path arg for dfs, just init it before dfs call

Similar:
- [ ] I've seen one before ?!
- 200 (DFS CC, hiepit impl)
- 711. Number of Distinct Islands II (allows rotate/reflection)
"""

from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def os_normalize():
            """
            A frozenset is an immutable set.
            T: O(MN)
            """
            m, n = len(grid), len(grid[0])

            def dfs(i, j):
                if not (0 <= i < m and 0 <= j < n) or grid[i][j] == 0:
                    return
                grid[i][j] = 0
                path.add((i - row_ori, j - col_ori))
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    dfs(i + dx, j + dy)

            unique_islands = set()
            for i in range(m):
                for j in range(n):
                    path = set()
                    row_ori, col_ori = i, j
                    dfs(i, j)
                    if path:
                        unique_islands.add(frozenset(path))
            print(unique_islands)
            return len(unique_islands)

        def os_path_signature():
            """
            Runtime: 303 ms, faster than 41.78% of Python3 online submissions for Number of Distinct Islands.

            T: O(MN), M:O(MN)
            """
            m, n = len(grid), len(grid[0])
            # dfs to find all cells in the current island
            def dfs(i, j, d):
                if not (0 <= i < m and 0 <= j < n):
                    return
                if (i, j) in vis or not grid[i][j]:
                    return
                vis.add((i, j))
                path_signature.append(d)
                dfs(i + 1, j, "D")
                dfs(i - 1, j, "U")
                dfs(i, j + 1, "R")
                dfs(i, j - 1, "L")
                # '.' means backtrack
                path_signature.append(".")

            # repeatedly start DFS as long as there're islands remaining
            vis = set()
            unique_islands = {}
            for i in range(m):
                for j in range(n):
                    path_signature = []
                    dfs(i, j, "")
                    if path_signature:
                        sig = "".join(path_signature)
                        unique_islands[sig] = None
            print(unique_islands)
            return len(unique_islands)

        return os_path_signature()
        # return os_normalize()


sl = Solution()
grid = [
    [1, 1, 0, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 0, 0, 1, 0],
]
# grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
# grid=[[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
print(sl.numDistinctIslands(grid))
