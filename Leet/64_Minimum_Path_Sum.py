"""
https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
Day 13: Min/Max Path Sum

"""


from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # TODO: as OS mentioned, for minimum path to destination, we should traverse from destination!
        #       also optimize to 1D array DP.
        def fxr():
            """
            Runtime: 92 ms, faster than 94.17% of Python3 online submissions for Minimum Path Sum.

            AC in 1.
            """
            m, n = len(grid), len(grid[0])
            F = [[0] * n for _ in range(m)]
            F[0][0] = grid[0][0]
            # for c in range(1, n):
            #     F[0][c] = F[0][c-1]+grid[0][c]
            # for r in range(1, m):
            #     F[r][0] = F[r-1][0] + grid[r][0]

            for i in range(m):
                for j in range(n):
                    if i + j == 0:
                        continue
                    elif i == 0:
                        F[i][j] = F[i][j - 1] + grid[i][j]
                    elif j == 0:
                        F[i][j] = F[i - 1][j] + grid[i][j]
                    else:
                        F[i][j] = min(F[i - 1][j], F[i][j - 1]) + grid[i][j]

            return F[m - 1][n - 1]

        return fxr()


sl = Solution()
print(sl.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(sl.minPathSum(grid=[[1, 2, 3], [4, 5, 6]]))
