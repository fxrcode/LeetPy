"""
tag: medium, skills
Lookback
- must be strong in basic skill
Similar:
- 54. Spiral Matrix
- 1886.
- 1492. The kth Factor of n

https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

TODO: diagonal
"""


from typing import List


class Solution:
    def rotate(self, M: List[List[int]]) -> None:
        """
        Runtime: 40 ms, faster than 77.58% of Python3 online submissions for Rotate Image.

        Do not return anything, modify matrix in-place instead.
        """
        """
        def rot90_tup4_Cpp(i, j, n):
            # BUG: A, B, C, D = (i, j), (j, n), (n, n-j), (n-j, i)
            # BUG: A, B, C, D = (i, j), (j, n - i), (n - i, n - j), (n - j, i)
            tmp = M[i][j]
            M[i][j] = M[n - j - 1][i]
            M[n - j - 1][i] = M[n - i - 1][n - j - 1]
            M[n - i - 1][n - j - 1] = M[j][n - i - 1]
            M[j][n - i - 1] = tmp
        """

        n = len(M)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                # A,B,C,D = D,A,B,C
                # RHS evaluated first, then assign to LHS
                # Swapping Values WithoutUsing a Temporary Variable
                M[i][j], M[j][n - i - 1], M[n - i - 1][n - j - 1], M[n - j - 1][i] = M[n - j - 1][i], M[i][j], M[j][n - i - 1], M[n - i - 1][n - j - 1]


"""
def left_up_quarter(n):
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            print(i, j)
"""


sl = Solution()
# matrix = [[1, 2], [3, 4]]
# sl.rotate(matrix)
# print(matrix)

matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
sl.rotate(matrix)
print(matrix)
