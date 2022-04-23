'''
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming
'''
from typing import List

INF = 1e6


class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        def clean_dibdidib():
            """
            Runtime: 152 ms, faster than 36.56% of Python3 online submissions for Minimum Falling Path Sum.

            https://leetcode.com/problems/minimum-falling-path-sum/discuss/186666/C++Java-4-lines-DP/218290

            XXX: pythonic list comprehension is so elegant!
            YYY: the smell part is overwrite input
            """
            m, n = len(mat), len(mat[0])
            for i in range(1, m):
                for j in range(n):
                    mat[i][j] += min(mat[i-1][k]
                                     for k in (j-1, j, j+1) if 0 <= k < n)
            return min(mat[-1])

        def fxr_dp():
            """
            Runtime: 152 ms, faster than 36.56% of Python3 online submissions for Minimum Falling Path Sum.

            AC in 1.
            T: O(MN), M: O(N)
            """
            m, n = len(mat), len(mat[0])
            F = [[INF] * n for _ in range(2)]  # min falling path sum to (i,j)
            for c in range(n):
                F[0][c] = mat[0][c]
            for r in range(1, m):
                for c in range(n):
                    prev = [F[(r-1) % 2][c]]
                    if c-1 >= 0:
                        prev.append(F[(r-1) % 2][c-1])
                    if c+1 < n:
                        prev.append(F[(r-1) % 2][c+1])
                    F[r % 2][c] = mat[r][c] + min(prev)
            return min(F[(m-1) % 2])
        # return fxr_dp()
        return clean_dibdidib()


sl = Solution()
print(sl.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
print(sl.minFallingPathSum([[-19, 57], [-40, -5]]))
