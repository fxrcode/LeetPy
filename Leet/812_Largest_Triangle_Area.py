"""
tag: Easy, Math
Lookback:
- From lee215 #1037
Similar:
- 976. Largest Perimeter Triangle
"""


from itertools import combinations
from typing import List


class Solution:
    def largestTriangleArea(self, p: List[List[int]]) -> float:
        def lee215():
            """
            https://www.cuemath.com/geometry/area-of-triangle-in-coordinate-geometry/
            Runtime: 254 ms, faster than 31.66% of Python3 online submissions for Largest Triangle Area.
            """
            # for i in p:
            #     for j in p:
            #         for k in p:
            res = max(0.5 * abs(i[0] * j[1] + j[0] * k[1] + k[0] * i[1] - j[0] * i[1] - k[0] * j[1] - i[0] * k[1]) for i, j, k in combinations(p, 3))
            return res

        return lee215()


sl = Solution()
print(sl.largestTriangleArea(p=[[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))
