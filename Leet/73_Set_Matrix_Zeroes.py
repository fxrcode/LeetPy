"""
https://leetcode.com/list?selectedList=99566jt7
Neetcode Blind Curated 75


"""


from typing import List


class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def fxr():
            """
            Runtime: 124 ms, faster than 92.61% of Python3 online submissions for Set Matrix Zeroes.

            T: O(m+n), M: O(mn)
            """
            m, n = len(mat), len(mat[0])
            M, N = [0] * m, [0] * n
            for r in range(m):
                for c in range(n):
                    if mat[r][c] == 0:
                        M[r] = 1
                        N[c] = 1
            for i in range(m):
                if M[i] == 1:
                    for j in range(n):
                        mat[i][j] = 0
            for j in range(n):
                if N[j] == 1:
                    for i in range(m):
                        mat[i][j] = 0

        def os():
            """
            Runtime: 124 ms, faster than 92.61% of Python3 online submissions for Set Matrix Zeroes.

            XXX: Good basic coding
            """
            first_col = False
            m, n = len(mat), len(mat[0])
            for r in range(m):
                if mat[r][0] == 0:
                    first_col = True
                for c in range(1, n):
                    if mat[r][c] == 0:
                        mat[r][0] = 0
                        mat[0][c] = 0
                        # BUG: !!! careful in flagging!
                        # if c == 0:
                        #     first_col = True

            print(mat, first_col)

            for r in range(1, m):
                for c in range(1, n):
                    if not mat[r][0] or not mat[0][c]:
                        mat[r][c] = 0

            # see if 1st row needs 0 out
            if mat[0][0] == 0:
                for c in range(n):
                    mat[0][c] = 0

            # see if 1st col needs 0 out
            if first_col:
                for r in range(m):
                    mat[r][0] = 0

        def osss():
            """
            :type matrix: List[List[int]]
            :rtype: void Do not return anything, modify matrix in-place instead.
            """
            matrix = mat
            is_col = False
            R = len(matrix)
            C = len(matrix[0])
            for i in range(R):
                # Since first cell for both first row and first column is the same i.e. matrix[0][0]
                # We can use an additional variable for either the first row/column.
                # For this solution we are using an additional variable for the first column
                # and using matrix[0][0] for the first row.
                if matrix[i][0] == 0:
                    is_col = True
                for j in range(1, C):
                    # If an element is zero, we set the first element of the corresponding row and column to 0
                    if matrix[i][j] == 0:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
            print(matrix)

            # Iterate over the array once again and using the first row and first column, update the elements.
            for i in range(1, R):
                for j in range(1, C):
                    if not matrix[i][0] or not matrix[0][j]:
                        matrix[i][j] = 0

            # See if the first row needs to be set to zero as well
            if matrix[0][0] == 0:
                for j in range(C):
                    matrix[0][j] = 0

            # See if the first column needs to be set to zero as well
            if is_col:
                for i in range(R):
                    matrix[i][0] = 0

        os()
        # osss()


sl = Solution()
mat = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
sl.setZeroes(mat)
print(mat)
