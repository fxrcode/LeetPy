"""
tag: Medium, sweep-line
Lookback:
- AC in 3min
"""

from typing import List


class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        def fxr():
            """
            Runtime: 2310 ms, faster than 13.94% of Python3 online submissions for Brightest Position on Street.

            sweep-line
            """
            points = []
            for p, r in lights:
                points.append((p - r, -1))
                points.append((p + r, 1))
            points.sort()
            mx = 0
            ans = -2e9
            sm = 0
            for i, flag in points:
                sm += 1 if flag == -1 else -1
                if sm > mx:
                    mx = sm
                    ans = i
            return ans

        return fxr()


sl = Solution()
print(sl.brightestPosition(lights=[[-3, 2], [1, 2], [3, 3]]))
print(sl.brightestPosition(lights=[[1, 0], [0, 1]]))
print(sl.brightestPosition(lights=[[1, 2]]))
