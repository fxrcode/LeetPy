"""
✅ GOOD Hash (set of frozensets)
Tag: Hard, DFS
Lookback:
- 694's path signature might not be easy fit in 711. Actually os2 in 694: normalization is better suit.
- learn about coord change in rotate & reflect.
- 1st time `frozenset`
- same as 694, we don't need path arg for dfs, just init it before dfs call
Similar:
- 694
- 200
"""

from typing import List


class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        def ryanleitaiwan_norm():
            """
            Runtime: 467 ms, faster than 68.85% of Python3 online submissions for Number of Distinct Islands II.

            T: O(MN)
            https://leetcode.com/problems/number-of-distinct-islands-ii/discuss/1515867/Python3-O(mn)-Well-Explained%3A-DFS-%2B-Hash-Set-of-Relative-Transformed-Coordinates
            4 for rotate: rotate_0 = [+r, +c]; rotate_90 = [-c, +r]; rotate_180 = [-r, -c]; rotate_270 = [+c, -r]
            4 for reflect: reflect_r = [-r, +c]; reflect_c = [+r, -c]; reflect_rc = [+c, +r]; reflect_minus_rc = [-c, -r]
                                   |     * (-2, 1) of 90 deg
             (-1, -2) of 180 deg   |
                        *          |
                                   |
            -----------------------+-----------------------> +c
                                   |
                                   |          * (1, 2) of 0 deg
                                   |
                             *     |
               (2, -1) of 270 deg  v
                                   +r
            """
            m, n = len(grid), len(grid[0])

            def dfs(i, j):
                if not (0 <= i < m and 0 <= j < n) or grid[i][j] == 0:
                    return
                grid[i][j] = 0
                path.append((i - row_ori, j - col_ori))
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    dfs(i + dx, j + dy)

            def norm(path):
                rs, cs = zip(*path)  # Unzip path by calling zip(*path)
                rmin, cmin = min(rs), min(cs)
                return frozenset([(r - rmin, c - cmin) for r, c in path])

            unique_islands = set()
            for i in range(m):
                for j in range(n):
                    path = []
                    row_ori, col_ori = i, j
                    dfs(i, j)
                    if not path:
                        continue
                    trans = []
                    trans.append(norm([(+r, +c) for r, c in path]))
                    trans.append(norm([(+r, -c) for r, c in path]))
                    trans.append(norm([(-r, +c) for r, c in path]))
                    trans.append(norm([(-r, -c) for r, c in path]))
                    trans.append(norm([(+c, +r) for r, c in path]))
                    trans.append(norm([(+c, -r) for r, c in path]))
                    trans.append(norm([(-c, +r) for r, c in path]))
                    trans.append(norm([(-c, -r) for r, c in path]))
                    unique_islands.add(frozenset(trans))
            return len(unique_islands)

        return ryanleitaiwan_norm()


sl = Solution()
grid = [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]]
print(sl.numDistinctIslands2(grid))
