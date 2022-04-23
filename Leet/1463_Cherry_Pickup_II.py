"""
✅ GOOD DP (states analysis)
Daily Challenge (Jan 8)
"""

from typing import List
from functools import cache


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def os_sync():
            """
            Runtime: 792 ms, faster than 92.45% of Python3 online submissions for Cherry Pickup II.

            T: O(MN^2)
            XXX: We aim to apply DP, so we are looking for an order that suitable for DP.
            Q: Can we move robot1 to the bottom firstly, then move robot2? NO
            A: Maybe not. In this case, the movement of robot1 will impact the movement of robot2.
                In other words, the optimal track of robot2 depends on the track of robot1. If we want
                to apply DP, we need to record the whole track of robot1 as the state.
                The number of sub-problems is too much.
            """
            m, n = len(grid), len(grid[0])

            @cache
            def dp(row, col1, col2):
                if not (0 <= col1 < n and 0 <= col2 < n):
                    return -1e9
                # current cell
                result = 0
                result += grid[row][col1]
                if col1 != col2:
                    result += grid[row][col2]
                # transition
                if row != m - 1:
                    result += max(
                        dp(row + 1, new_col1, new_col2)
                        for new_col1 in [col1, col1 + 1, col1 - 1]
                        for new_col2 in [col2, col2 + 1, col2 - 1]
                    )
                return result

            return dp(0, 0, n - 1)

        return os_sync()


sl = Solution()
print(
    sl.cherryPickup(
        grid=[
            [1, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 3, 0],
            [2, 0, 9, 0, 0, 0, 0],
            [0, 3, 0, 5, 4, 0, 0],
            [1, 0, 2, 3, 0, 0, 6],
        ]
    )
)

