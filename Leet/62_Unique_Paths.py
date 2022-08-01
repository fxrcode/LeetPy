"""
Tag: Medium, DP, Math
Lookback:
- Top 100 Liked Questions
- Top-down DP === Reverse Thinking
"""


from functools import cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def fxr_topdown():
            """
            Runtime: 37 ms, faster than 84.11% of Python3 online submissions for Unique Paths.

            """
            DIR = [(0, 1), (1, 0)]

            @cache
            def dp(i, j):
                if (i, j) == (0, 0):
                    return 1

                ans = 0
                for dx, dy in DIR:
                    ii, jj = i - dx, j - dy
                    if 0 <= ii < m and 0 <= jj < n:
                        ans += dp(ii, jj)
                return ans

            return dp(m - 1, n - 1)

        return fxr_topdown()

        def fxr_tabu():
            """
            Runtime: 28 ms, faster than 90.75% of Python3 online submissions for Unique Paths.

            AC in 1.
            """
            # BUG: Rolling arrays optimize ROW only!!!
            #  F = [[0]*2 for _ in range(2)]
            F = [[0] * n for _ in range(2)]

            for i in range(m):
                for j in range(n):
                    if i == 0 or j == 0:
                        F[i % 2][j] = 1
                    else:
                        F[i % 2][j] = F[(i - 1) % 2][j] + F[i % 2][j - 1]
            return F[(m - 1) % 2][n - 1]


sl = Solution()
assert sl.uniquePaths(m=3, n=7) == 28
print(sl.uniquePaths(m=3, n=2))
