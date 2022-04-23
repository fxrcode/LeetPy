"""
Google tag
tag: easy

Lookback:
- Transform/re-state problem, rather simulate
- odd element => (oddRow,evenCol) or (evenRow,oddCol), do the count
"""

from collections import Counter
from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        def rock():
            """
            Runtime: 40 ms, faster than 93.14% of Python3 online submissions for Cells with Odd Values in a Matrix.

            XXX: odd_rows * even_cols + even_rows * odd_cols
            T: O(L + m + n), M: O(m + n), where L = indices.length.
            """
            oddRows, oddCols = [False] * m, [False] * n
            for r, c in indices:
                oddRows[r] ^= True
                oddCols[c] ^= True
            cntRow = sum(oddRows)
            cntCol = sum(oddCols)
            evenRows = m - cntRow
            evenCols = n - cntCol
            return evenCols * cntRow + evenRows * cntCol

        def fxr():
            """
            Runtime: 102 ms, faster than 10.77% of Python3 online submissions for Cells with Odd Values in a Matrix.

            T: O(mn + indices)
            """
            row, col = Counter(), Counter()
            for r, c in indices:
                row[r] += 1
                col[c] += 1
            ans = 0
            for i in range(m):
                for j in range(n):
                    if (row[i] + col[j]) % 2:
                        ans += 1
            return ans
