"""
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

tag: easy, skills
Lookback
- still led by the nose
- Crux: (r,c) <-> idx <-> (r',c')
"""

from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        def hiepit():
            """
            Runtime: 88 ms, faster than 92.57% of Python3 online submissions for Reshape the Matrix.

            https://leetcode.com/problems/reshape-the-matrix/discuss/1317225/Python-One-pass-Clean-and-Concise

            """
            m, n = len(mat), len(mat[0])
            if r * c != m * n:
                return mat  # Invalid size -> return original matrix
            ans = [[0] * c for _ in range(r)]
            for i in range(m * n):
                ans[i // c][i % c] = mat[i // n][i % n]
            return ans

        def fxr():
            """
            Runtime: 124 ms, faster than 53.97% of Python3 online submissions for Reshape the Matrix.

            """
            res = [[0] * c for _ in range(r)]
            R, C = len(mat), len(mat[0])
            if r * c != R * C:
                return mat
            for i in range(R):
                for j in range(C):
                    idx = i * C + j
                    x, y = divmod(idx, c)
                    res[x][y] = mat[i][j]
            return res
