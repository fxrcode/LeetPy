"""
tag: easy
Lookback:
- This is a copycat question to 531. Lonely Pixel I.
"""

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def fxr():
            # Runtime: 199 ms, faster than 74.11% of Python3 online submissions for Special Positions in a Binary Matrix.
            m, n = len(mat), len(mat[0])
            rows, cols = [0] * m, [0] * n
            for i in range(m):
                for j in range(n):
                    if mat[i][j] == 1:
                        rows[i] += 1
                        cols[j] += 1
            cnt = 0
            for i in range(m):
                for j in range(n):
                    if mat[i][j] == 1:
                        if rows[i] == cols[j] == 1:
                            cnt += 1
            return cnt
