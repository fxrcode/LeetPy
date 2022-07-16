"""
✅ GOOD DP (Matrix, path)
Tag: Medium, DP
Lookback:
- I defined dp func as dp(i,j,left,prev), reminds me TSP, 1197,1654, 863, but it's WRONG! no need of prev. WHY?
[ ] REDO
"""


from functools import cache


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        def hiepit():
            DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            @cache
            def dp(i, j, left):
                """
                dp be the # of paths if we start from (i,j) and we have left steps to go.
                """
                # if left == 0:
                #     return 0
                if not (0 <= i < m and 0 <= j < n):
                    return 1
                if left == 0:
                    return 0
                res = 0
                for dx, dy in DIR:
                    r, c = dx + i, dy + j
                    res += dp(r, c, left - 1)
                return res % 1_000_000_007

            return dp(startRow, startColumn, maxMove)

        return hiepit()


sl = Solution()
print(sl.findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0))
print(sl.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1))
