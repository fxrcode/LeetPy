"""
✅ GOOD DFS (path signature)
Tag: Medium, DFS, Hash
Lookback:
- classic Grid Path Signature
Similar:
- [ ] I've seen one before ?!
- 200 (DFS CC, hiepit impl)
- 711. Number of Distinct Islands II (allows rotate/reflection)

"""

from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
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
                # 'x' means backtrack
                path_signature.append("x")

            # repeatedly start DFS as long as there're islands remaining
            vis = set()
            unique_islands = set()
            for i in range(m):
                for j in range(n):
                    path_signature = []
                    dfs(i, j, "")
                    if path_signature:
                        sig = "".join(path_signature)
                        unique_islands.add(sig)
            # print(unique_islands)
            return len(unique_islands)

        return os_path_signature()


sl = Solution()
grid = [
    [1, 1, 0, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 0, 0, 1, 0],
]
# grid=[[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
print(sl.numDistinctIslands(grid))
