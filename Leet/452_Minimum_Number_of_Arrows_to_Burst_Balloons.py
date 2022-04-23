"""
✅ GOOD Greedy
Daily Challenge (Jan 13)
Labuladong P381: Greedy (Interval Scheduling)
tag: medium, Greedy
"""

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def intervalSchedule():
            """ "
            Runtime: 1236 ms, faster than 93.30% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.

            T: O(N)
            """
            itvs = sorted(points, key=lambda li: li[1])
            x_end = itvs[0][1]
            count = 1
            for start, end in itvs:
                if start > x_end:
                    count += 1
                    x_end = end
            return count

        return intervalSchedule()


sl = Solution()
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
points = [[1, 2], [3, 4], [5, 6], [7, 8]]
points = [[1, 2], [2, 3], [3, 4], [4, 5]]

print(sl.findMinArrowShots(points))
