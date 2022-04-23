'''
Google | Phone | Finding squares in a 2D grid

https://leetcode.com/discuss/interview-question/573940/google-phone-finding-squares-in-a-2d-grid
'''

from typing import List
from collections import defaultdict


class Solution:
    def largest1BorderedSquare(self, M: List[List[int]]) -> int:
        def fxr_SOF():
            """
            Runtime: 992 ms, faster than 14.69% of Python3 online submissions for Largest 1-Bordered Square.

            XXX: Calculate cumulative sums by rows and by columns
            Then loop all left-upper corner and possible square len to check ALL-4 side len
            https://stackoverflow.com/questions/63734577/count-the-squares-in-the-grid
            """
            m, n = len(M), len(M[0])
            print(m, n)
            R, C = defaultdict(int), defaultdict(int)
            def nonzero(i, j): return 1 if M[i][j] in {1, '.', '+'} else 0

            mx_side = 0
            SQ = []  # (upper-left, side-length)
            for i in range(m):
                for j in range(n):
                    v = nonzero(i, j)
                    R[i, j] = R[i, j-1] + v
                    C[i, j] = C[i-1, j] + v
            for i in range(m):
                for j in range(n):
                    if not nonzero(i, j):
                        continue
                    for k in range(min(m-i, n-j)):
                        # for k in range(min(m-i, n-j)-1, 0, -1):
                        # print(list(range(1, min(m-i, n-j))), k)
                        if nonzero(i+k, j+k) == 0:
                            continue
                        # top row
                        if R[i, j+k] - R[i, j] != k:
                            # BUG: break. Should be continue, we should try next side-length!
                            continue  # there's hole, so no need to check other side,
                        # left column
                        if C[i+k, j] - C[i, j] != k:
                            # break
                            continue
                        # bottom row
                        if R[i+k, j+k] - R[i+k, j] != k:
                            # break
                            continue
                        # right column
                        if C[i+k, j+k] - C[i, j+k] != k:
                            # break
                            continue
                        SQ.append((i, j, k+1))
                        mx_side = max(mx_side, k+1)
            # print(SQ)
            return mx_side**2
        return fxr_SOF()
        '''
            L = [[0] * n for _ in range(m)]
            R = [[0] * n for _ in range(m)]
            U = [[0] * n for _ in range(m)]
            D = [[0] * n for _ in range(m)]
            L, R, U, D = defaultdict()
            for i in range(m):
                for j in range(n):
                    if M[i][j] == 1:
                        L[i, j] = L[i-1, j] + 1
                        U[i, j] = U[i, j-1] + 1
                        R[~i, ~j] = R[~i, ~j+1] + 1
                        D[~i, ~j] = D[~i+1, ~j] + 1
            '''


sl = Solution()
# a = ['......', '. .  .', '...  .', '. ....', '......']
M = [[0, 0, 0, 1]]
# M = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
# M = [[1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1], [
#     1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0]]
print(sl.largest1BorderedSquare(M))
