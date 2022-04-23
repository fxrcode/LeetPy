"""
Tag: Medium, Matrix
Lookback:
- I used FSM but still complicate. 
- DBabichev's DIR trick is neat
- Daily Challenge (04132022)
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def dbabichev():
            """
            Runtime: 31 ms, faster than 92.43% of Python3 online submissions for Spiral Matrix II.

            Common trick of Matrix: https://leetcode.com/problems/spiral-matrix-ii/discuss/963128/Python-rotate-when-need-explained
            (0,1) => (1,0) => (0,-1) => (-1,0)
            """
            M = [[0] * n for _ in range(n)]
            x, y, dx, dy = 0, 0, 0, 1
            for i in range(n * n):
                M[x][y] = i + 1
                if not 0 <= x + dx < n or not 0 <= y + dy < n or M[x + dx][y + dy] != 0:
                    dx, dy = dy, -dx
                x, y = x + dx, y + dy
            return M

        return dbabichev()

        def fxr():
            # Runtime: 26 ms, faster than 97.33% of Python3 online submissions for Spiral Matrix II.
            st = 0  # 0: right, 1: down, 2: left: 3: up
            M = [[0] * n for _ in range(n)]
            L, R, U, B = 0, n - 1, 0, n - 1
            r, c = 0, 0
            for v in range(1, n * n + 1):
                # r, c = divmod(co, n)
                M[r][c] = v
                if st == 0:
                    c += 1
                    if c == R:
                        st = (st + 1) % 4
                        U += 1
                elif st == 1:
                    r += 1
                    if r == B:
                        st = (st + 1) % 4
                        R -= 1
                elif st == 2:
                    c -= 1
                    if c == L:
                        st = (st + 1) % 4
                        B -= 1
                else:
                    r -= 1
                    if r == U:
                        st = (st + 1) % 4
                        L += 1

            return M

        return fxr()


sl = Solution()
print(sl.generateMatrix(n=3))
print(sl.generateMatrix(n=1))
print(sl.generateMatrix(n=5))
