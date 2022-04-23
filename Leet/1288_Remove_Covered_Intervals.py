"""
tag: medium, Interval 
Lookback:
- intervals 3 types: 1288, 56, 986
"""

from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def fxr():
            """
            Runtime: 138 ms, faster than 49.34% of Python3 online submissions for Remove Covered Intervals.

            AC in 1.
            T: O(NlogN)
            """
            intervals.sort(key=lambda x: (x[0], -x[1]))
            # x, y = -1, -1
            pre_end = 0
            res = 0
            for _, r in intervals:
                if r > pre_end:
                    pre_end = r
                    res += 1

            return res

        return fxr()


sl = Solution()
# intervals = [[1, 4], [3, 6], [2, 8]]
intervals = [[1, 4], [2, 3]]
print(sl.removeCoveredIntervals(intervals))
