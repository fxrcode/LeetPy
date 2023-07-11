"""
✅ GOOD Matrix
Tag: Medium, Skill, Matrix
Lookback:
- rotate list: arr = arr[k:] + arr[:k]
"""

from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def ye15():
            """
            Runtime: 233 ms, faster than 51.83% of Python3 online submissions for Cyclically Rotating a Grid.

            T: O(mn)
            """
            m, n = len(grid), len(grid[0])
            T, L = 0, 0
            B, R = m - 1, n - 1
            while T < B and L < R:
                path = []
                for c in range(L, R):
                    path.append(grid[T][c])
                for r in range(T, B):
                    path.append(grid[r][R])
                for c in range(R, L, -1):
                    path.append(grid[B][c])
                for r in range(B, T, -1):
                    path.append(grid[r][L])

                kk = k % len(path)
                path = path[kk:] + path[:kk]  # trick of rotate array: O(1)
                i = 0
                for c in range(L, R):
                    grid[T][c] = path[i]
                    i += 1
                for r in range(T, B):
                    grid[r][R] = path[i]
                    i += 1
                for c in range(R, L, -1):
                    grid[B][c] = path[i]
                    i += 1
                for r in range(B, T, -1):
                    grid[r][L] = path[i]
                    i += 1
                T, L = T + 1, L + 1
                B, R = B - 1, R - 1

            return grid

        return ye15()

        def yajassardana():
            """
            Runtime: 576 ms, faster than 12.80% of Python3 online submissions for Cyclically Rotating a Grid.

            T: O(mnk)
            """
            m, n = len(grid), len(grid[0])
            T, L = 0, 0
            B, R = m - 1, n - 1

            while T < B and L < R:
                no_elems = 2 * (B - T + 1) + 2 * (R - L + 1) - 4
                no_rotate = k % no_elems
                for _ in range(no_rotate):
                    tmp = grid[T][L]
                    for j in range(L, R):
                        grid[T][j] = grid[T][j + 1]
                    for i in range(T, B):
                        grid[i][R] = grid[i + 1][R]
                    for j in range(R, L, -1):
                        grid[B][j] = grid[B][j - 1]
                    for i in range(B, T, -1):
                        grid[i][L] = grid[i - 1][L]
                    grid[T + 1][L] = tmp
                T, L = T + 1, L + 1
                B, R = B - 1, R - 1
            return grid

        return yajassardana()


sl = Solution()
print(
    sl.rotateGrid(
        grid=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], k=2
    )
)
