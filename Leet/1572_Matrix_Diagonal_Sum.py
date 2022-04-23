"""
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

tag: easy, skills
Lookback:
- why bitmask DFS is O(2^N*N^2) vs DFS is O(N^2), given they both try all possiblity?
    - this simple matrix loop gives good example, don't be led by the nose by leetcode!
"""

from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        def brianchiang_tw():
            """
            Runtime: 120 ms, faster than 77.27% of Python3 online submissions for Matrix Diagonal Sum.

            T:O(N)
            """
            N = len(mat)
            ans = 0
            for i in range(N):
                ans += mat[i][i]
                ans += mat[N - 1 - i][i]
            if N % 2 == 1:
                ans -= mat[N // 2][N // 2]
            return ans

        def fxr():
            """
            Runtime: 209 ms, faster than 13.58% of Python3 online submissions for Matrix Diagonal Sum.

            T:O(N^2)
            """
            N = len(mat)
            ans = 0
            for r in range(N):
                for c in range(N):
                    if r == c:
                        ans += mat[r][c]
                    if r + c == N - 1:
                        ans += mat[r][c]
            if N % 2 == 1:
                ans -= mat[N // 2][N // 2]
            return ans
