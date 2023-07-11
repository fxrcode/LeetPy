"""
tag: medium, hash
Lookback:
- same as 1380, after understand the problem
"""

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        def fxr():
            # Runtime: 76 ms, faster than 92.24% of Python3 online submissions for Max Increase to Keep City Skyline.
            mxr = [max(row) for row in grid]
            mxc = [max(col) for col in zip(*grid)]

            gain = 0
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    gain += min(mxr[r], mxc[c]) - grid[r][c]
            return gain

        return fxr()


sl = Solution()
print(
    sl.maxIncreaseKeepingSkyline(
        grid=[[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    )
)
assert sl.maxIncreaseKeepingSkyline(grid=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
