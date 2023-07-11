"""
✅ GOOD Matrix (loop)
💡insight

FB tag (6mo)

Follow up:
* What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
* What if the matrix is so large that you can only load up a partial row into the memory at once?
"""


from collections import deque
from typing import List


class Solution:
    def isToeplitzMatrix(self, M: List[List[int]]) -> bool:
        def fu1():
            """
            Runtime: 80 ms, faster than 90.92% of Python3 online submissions for Toeplitz Matrix.

            https://leetcode.com/problems/toeplitz-matrix/discuss/516366/Python-Follow-Up-1-with-Explanation-and-Diagrams
            💡!SMART
            """
            if not M or not M[0]:
                return False

            expected = deque(M[0])
            for r in range(1, len(M)):
                row = M[r]
                expected.pop()
                expected.appendleft(row[0])

                for c in range(1, len(row)):
                    if row[c] != expected[c]:
                        return False
            return True

        def fxr():
            m, n = len(M), len(M[0])
            for i in range(m - 1):
                for j in range(n - 1):
                    if M[i][j] != M[i + 1][j + 1]:
                        return False
            return True

        return fxr()


sl = Solution()
print(sl.isToeplitzMatrix([[11, 74, 0, 93], [40, 11, 74, 7]]))
