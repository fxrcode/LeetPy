"""
✅ GOOD Greedy
Daily Challenge (01/13/2022:01/04/2023)
Labuladong P381: Greedy (Interval Scheduling)
tag: medium, Greedy
"""

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def intervalSchedule():
            """ "
            https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/887690/Python-O(n-log-n)-solution-explained
            Runtime: 1236 ms, faster than 93.30% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.

            T: O(N)
            """
            points.sort(key = lambda x: x[1])
            n, count = len(points), 1
            if n == 0: return 0
            curr = points[0]

            for i in range(n):
                if curr[1] < points[i][0]:
                    count += 1
                    curr = points[i]

            return count

        return intervalSchedule()


sl = Solution()
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
points = [[1, 2], [3, 4], [5, 6], [7, 8]]
points = [[1, 2], [2, 3], [3, 4], [4, 5]]

print(sl.findMinArrowShots(points))
