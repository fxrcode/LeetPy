"""
tag: medium, sort
Lookback:


similar: 
1570. sparse vector dot product
"""

from collections import defaultdict
from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def ruifeng_optimal():
            """
            https://leetcode.com/problems/sparse-matrix-multiplication/discuss/577491/4-python-approaches-with-time-and-space-analysis
            T: O(N). N = non-zeros in mat1 + mat2
            TODO:
            """

        def ruifeng_app3():
            """
            Runtime: 63 ms, faster than 86.14% of Python3 online submissions for Sparse Matrix Multiplication.

            T: O(IJ+JK+sparsity)
            """

            def get_none_zero(mat):
                coord = {}
                rows, cols = len(mat), len(mat[0])
                for r in range(rows):
                    for c in range(cols):
                        if mat[r][c] != 0:
                            coord[(r, c)] = mat[r][c]
                return coord

            sparse_A, sparse_B = get_none_zero(mat1), get_none_zero(mat2)

            m, k, n = len(mat1), len(mat1[0]), len(mat2[0])

            res = [[0 for _ in range(n)] for _ in range(m)]

            for pos1, val1 in sparse_A.items():
                for pos2, val2 in sparse_B.items():
                    if pos1[1] == pos2[0]:
                        res[pos1[0]][pos2[1]] += val1 * val2

            return res

        return app3()

        def fxr():
            """
            Runtime: 56 ms, faster than 87.15% of Python3 online submissions for Sparse Matrix Multiplication.

            T: O(IJ+JK+NZ1+NZ2)
            """
            I, J = len(mat1), len(mat1[0])
            K = len(mat2[0])

            nz1 = defaultdict(set)
            for i in range(I):
                for j in range(J):
                    if mat1[i][j]:
                        nz1[j].add((i))

            nz2 = defaultdict(set)
            for j in nz1:
                for k in range(K):
                    if mat2[j][k]:
                        nz2[j].add((k))

            ans = [[0] * K for _ in range(I)]

            for j in nz1:
                for i in nz1[j]:
                    for k in nz2[j]:
                        ans[i][k] += mat1[i][j] * mat2[j][k]
            return ans

        return fxr()

        def classical():
            I, J = len(mat1), len(mat1[0])
            K = len(mat2[0])

            ans = [[0] * K for _ in range(I)]
            for i in range(I):
                for k in range(K):
                    for j in range(J):
                        ans[i][k] += mat1[i][j] * mat2[j][k]
            return ans

        return classical()


sl = Solution()
print(sl.multiply(mat1=[[1, 0, 0], [-1, 0, 3]], mat2=[[7, 0, 0], [0, 0, 0], [0, 0, 1]]))
print(sl.multiply([[1, -5]], [[12], [-1]]))
