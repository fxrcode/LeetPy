"""
tag: easy, hash
Lookback:
- similar: 807. Max Increase to Keep City Skyline
"""

from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        def rock():
            mnr = {min(row) for row in matrix}
            mxc = {max(col) for col in zip(*matrix)}
            return list(mnr & mxc)

        return rock()

        def fxr():
            # Runtime: 155 ms, faster than 72.73% of Python3 online submissions for Lucky Numbers in a Matrix.
            mnr = []
            res = []
            for r, row in enumerate(matrix):
                mnr.append(row.index(min(row)))
            for c, col in enumerate(zip(*matrix)):
                i = col.index(max(col))
                if mnr[i] == c:
                    res.append(matrix[i][c])
            return res

        return fxr()


sl = Solution()
print(sl.luckyNumbers(matrix=[[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
assert sl.luckyNumbers(matrix=[[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]) == [12]
assert sl.luckyNumbers(matrix=[[7, 8], [1, 2]]) == [7]
