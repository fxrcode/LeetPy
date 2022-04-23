"""
https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def fxr():
            """
            Runtime: 28 ms, faster than 90.75% of Python3 online submissions for Unique Paths.

            AC in 1.
            """
            # BUG: Rolling arrays optimize ROW only!!!
            #  F = [[0]*2 for _ in range(2)]
            F = [[0]*n for _ in range(2)]

            for i in range(m):
                for j in range(n):
                    if i == 0 or j == 0:
                        F[i % 2][j] = 1
                    else:
                        F[i % 2][j] = F[(i-1) % 2][j] + F[i % 2][j-1]
            return F[(m-1) % 2][n-1]

        return fxr()


sl = Solution()
print(sl.uniquePaths(m=3, n=7))
print(sl.uniquePaths(m=3, n=2))
