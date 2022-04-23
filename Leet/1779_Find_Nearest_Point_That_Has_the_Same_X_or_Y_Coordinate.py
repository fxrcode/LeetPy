from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def rock():
            """
            Runtime: 788 ms, faster than 73.95% of Python3 online submissions for Find Nearest Point That Has the Same X or Y Coordinate.

            """
            idx, mn = -1, 2e9
            for i, (r, c) in enumerate(points):
                dx, dy = x - r, y - c
                # at least one of them is zero, so take advantage of that.
                if dx * dy == 0 and abs(dx + dy) < mn:
                    mn = abs(dx + dy)
                    idx = i
            return idx
