"""
✅ GOOD Logic (use FSM solve problem methodically)
tag: medium, state-machine, skills
Lookback
- compare w/ 48. Rotate Image
Explore Array & String: 2D Array
https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1168/
Given an m x n matrix, return all elements of the matrix in spiral order.

"""


from typing import List


class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        def dbabichev_trick():
            """
            Runtime: 29 ms, faster than 89.65% of Python3 online submissions for Spiral Matrix.

            """
            m, n = len(matrix), len(matrix[0])
            DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            x, y = 0, 0
            dx, dy = DIR[0]
            di = 0
            ans = []
            for _ in range(m * n):
                if (
                    not (0 <= x + dx < m and 0 <= y + dy < n)
                    or matrix[x + dx][y + dy] == "*"
                ):
                    di = (di + 1) % 4
                    dx, dy = DIR[di]
                ans.append(matrix[x][y])
                matrix[x][y] = "*"
                x, y = x + dx, y + dy
            return ans

        return dbabichev_trick()

        def tech_dose_FSM():
            """
            Runtime: 32 ms, faster than 71.25% of Python3 online submissions for Spiral Matrix.
            TECH DOSE: Trick for spiral matrix traversal
            XXX: 1. top,bottom,left,right pointer. 2. use dir as state (if/elif). 3. stop when top/bottom and left/right crossed.
            """
            res = []
            top, bottom, left, right = 0, len(mat) - 1, 0, len(mat[0]) - 1
            dir = 0
            while top <= bottom and left <= right:
                # up
                if dir == 0:
                    for i in range(left, right + 1):
                        res.append(mat[top][i])
                    top += 1
                    dir += 1
                # right
                elif dir == 1:
                    for i in range(top, bottom + 1):
                        res.append(mat[i][right])
                    right -= 1
                    dir += 1
                # bottom
                elif dir == 2:
                    for i in range(right, left - 1, -1):
                        res.append(mat[bottom][i])
                    bottom -= 1
                    dir += 1
                # left
                elif dir == 3:
                    for i in range(bottom, top - 1, -1):
                        res.append(mat[i][left])
                    left += 1
                    dir = (dir + 1) % 4
            return res

    '''
    def spiralOrder_fxr(self, mat: List[List[int]]) -> List[int]:
        """
        Took a long time to code/debug to AC
        """
        Re, Cb, Re, Ce = 0, 0, len(mat), len(mat[0])
        # every hit, confine R/C l/r boundary
        total = Re*Ce
        res = []
        r, c = 0, 0
        while total:
            # Up (l->r)
            while c < Ce and total:
                print(mat[r][c], r, c)
                res.append(mat[r][c])
                c += 1
                total -= 1
            Re += 1
            # right (u->b)
            c -= 1
            r += 1
            while r < Re and total:
                print(mat[r][c], r, c)
                res.append(mat[r][c])
                r += 1
                total -= 1
            Ce -= 1
            # bottom (r->l)
            r -= 1
            c -= 1
            while c >= Cb and total:
                print(mat[r][c], r, c)
                res.append(mat[r][c])
                c -= 1
                total -= 1
            Re -= 1
            # left (b->u)
            r -= 1
            c += 1
            while r >= Re and total:
                print(mat[r][c], r, c)
                res.append(mat[r][c])
                r -= 1
                total -= 1
            Cb += 1
            # return
            r += 1
            c += 1
        return res
    '''


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sl = Solution()
print(sl.spiralOrder(matrix))
