"""
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

tag: easy, math
Lookback:
- even easy problem can separate 2k+ vs me... (much elegant & neat)
"""
import math
from typing import List


class Solution:
    def checkStraightLine(self, CO: List[List[int]]) -> bool:
        def rock():
            """
            https://leetcode.com/problems/check-if-it-is-a-straight-line/discuss/408984/JavaPython-3-check-slopes-short-code-w-explanation-and-analysis.

            + re-formulate slope from div to mul (prevent div-by-0)
            + slope(new co, (x0,y0)), rather slope(2 new co), less typing
            """
            (x0, y0), (x1, y1) = CO[:2]
            for x, y in CO:
                if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                    return False
            return True

        def fxr():
            def slope(P, Q):
                if P[0] == Q[0]:
                    return math.inf
                return (Q[1] - P[1]) / (Q[0] - P[0])

            sl = None
            for i in range(1, len(CO)):
                if i == 1:
                    sl = slope(CO[i], CO[i - 1])
                else:
                    if sl != slope(CO[i], CO[i - 1]):
                        return False
            return True

        return fxr()


sl = Solution()
coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
print(sl.checkStraightLine(coordinates))
