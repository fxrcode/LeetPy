"""
✅ GOOD Math (Group Action: Orbit-stabilizer)
tag: Easy, Math
Lookback:
- 2D version of 189. Rotate Array (Group Action)
Similar:
- 1914
"""

from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def os3_189_orbit_stabalizer():
            """
            Runtime: 160 ms, faster than 96.35% of Python3 online submissions for Shift 2D Grid.

            Group Theory: Group Action, orbit-stabilizer theorem
            https://leetcode.com/problems/rotate-array/solution/205266
            """
            nonlocal k
            m, n = len(grid), len(grid[0])
            k %= m * n

            start_idx, count = 0, 0
            while count < (m * n):
                cur_idx, pre_v = start_idx, grid[start_idx // n][start_idx % n]
                while True:
                    nxt_idx = (cur_idx + k) % (m * n)
                    i, j = divmod(nxt_idx, n)
                    grid[i][j], pre_v = pre_v, grid[i][j]
                    cur_idx = nxt_idx
                    count += 1
                    if cur_idx == start_idx:
                        break
                start_idx += 1
            return grid

        return os3_189_orbit_stabalizer()

        def os2_simulate():
            """
            XXX: this is more important to grasp
            """
            m, n = len(grid), len(grid[0])
            for _ in range(k):
                pre = grid[-1][-1]
                for i in range(m):
                    for j in range(n):
                        # !Crux
                        grid[i][j], pre = pre, grid[i][j]
            return grid

        return os2_simulate()

        def fxr():
            m, n = len(grid), len(grid[0])
            mn = m * n
            K = k % (mn)
            res = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    ij = i * n + j
                    xy = (ij + K) % mn
                    x, y = xy // n, xy % n
                    res[x][y] = grid[i][j]

            return res

        return fxr()


sl = Solution()
print(sl.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1))
print(
    sl.shiftGrid(
        grid=[[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], k=4
    )
)
