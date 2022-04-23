"""
tag: easy, array, skills
Lookback:
- 学会力扣OS的整行观察法找到坐标变换超级爽!
- vivek781113 is elegant!

Similar:
48. Rotate image
"""

from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def vivek781113():
            """
            https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/discuss/1589592/Key-points-or-Trick-or-Easy-to-remember-for-future
            key points : m = number of rows, n = number of colms
            rotate 90 deg once ->   i, j <--> j,  m - i - 1
            rotate 90 deg twice ->  i, j <--> m - i - 1, n - j - 1
            rotate 90 deg thrice -> i, j <--> n - j - 1, i
            """
            one = two = three = four = True
            m, n = len(mat), len(mat[0])
            for i in range(m):
                for j in range(n):
                    if mat[i][j] != target[j][m - i - 1]:
                        one = False
                    if mat[i][j] != target[m - i - 1][n - j - 1]:
                        two = False
                    if mat[i][j] != target[n - j - 1][i]:
                        three = False
                    if mat[i][j] != target[i][j]:
                        four = False
            return one or two or three or four

        return vivek781113()

        def fxr_48_rotate():
            """
            Runtime: 48 ms, faster than 76.80% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.

            """

            def rotate90():
                n = len(mat)
                for i in range(n // 2):
                    for j in range((n + 1) // 2):
                        mat[i][j], mat[j][n - i - 1], mat[n - i - 1][n - j - 1], mat[n - j - 1][i] = mat[n - j - 1][i], mat[i][j], mat[j][n - i - 1], mat[n - i - 1][n - j - 1]
                # [(i, j), (j, n - i - 1), (n - i - 1, n - j - 1), (n - j - 1, i)]

            n = len(mat)
            for _ in range(4):
                rotate90()
                if mat == target:
                    return True
            return False

        return fxr_48_rotate()

        def fxr_WA():
            """
            WA: [[1,1,1],[0,0,0],[0,0,0]]
                [[0,1,0],[0,0,0],[1,0,1]]
            BUG: my logic is like Rubik, not fully matched, only matching tuples...
            """

            def check_tuple(i, j, n):
                # i,j => j,n-i-1 =>n-i-1,n-j-1 => n-j-1,i
                idxs = [(i, j), (j, n - i - 1), (n - i - 1, n - j - 1), (n - j - 1, i)]

                src = [mat[r][c] for r, c in idxs] * 2
                tgt = [target[r][c] for r, c in idxs]
                # return tgt in src
                b, p = strStr(src, tgt)
                print(src, tgt, b, p)

                return b

            def strStr(src, tgt):
                for s in range(len(src) - len(tgt) + 1):
                    for i in range(len(tgt)):
                        if src[s + i] != tgt[i]:
                            break
                    else:
                        return True, s
                return False, -1

            n = len(mat)
            if n == 1:
                return mat[0] == target[0]
            for i in range(n // 2):
                for j in range((n + 1) // 2):
                    if not check_tuple(i, j, n):
                        return False
            return True


sl = Solution()
print(sl.findRotation(mat=[[1]], target=[[0]]))
print(sl.findRotation([[1, 1, 1], [0, 0, 0], [0, 0, 0]], [[0, 1, 0], [0, 0, 0], [1, 0, 1]]))
print(sl.findRotation(mat=[[0, 1], [1, 0]], target=[[1, 0], [0, 1]]))
print(sl.findRotation(mat=[[0, 1], [1, 1]], target=[[1, 0], [0, 1]]))
print(sl.findRotation(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]], target=[[1, 1, 1], [0, 1, 0], [0, 0, 0]]))
