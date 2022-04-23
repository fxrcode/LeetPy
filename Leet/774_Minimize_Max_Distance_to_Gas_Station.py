'''
✅ GOOD bisect
✅ GOOD DP (Knapsack)
tag: Hard, DP, bisect, Google
similar:
- 668
'''

from functools import cache
from math import ceil
from typing import List


class Solution:

    def minmaxGasDist(self, stations: List[int], k: int) -> float:

        def fun4LeetCode_bisect():
            """
            Approach the problem using the "trial and error" algorithm
            https://leetcode.com/problems/minimize-max-distance-to-gas-station/discuss/113629/Approach-the-problem-using-the-%22trial-and-error%22-algorithm
            XXX: 济公学院: 切分类generic bisect
            """
            l, r = 0, max(stations[i + 1] - stations[i] for i in range(len(stations) - 1))
            print(l, r)
            while r - l >= 1e-6:
                mid = (l + r) / 2.0
                cnt = 0
                for i in range(len(stations) - 1):
                    cnt += ceil((stations[i + 1] - stations[i]) / mid) - 1
                # print(mid, cnt)
                if cnt <= k:
                    r = mid
                else:
                    l = mid
            return l

        def fxr_knapsack():
            """
            TLE: 31 / 61 test cases passed.

            opt solution for adding g more stations in first n intervals.
            T: O(NK^2)            
            """
            deltas = []
            for l, r in zip(stations, stations[1:]):
                deltas.append(r - l)
            D = len(deltas)
            # print(deltas, D)

            @cache
            def dp(n, g):
                if n == 1:
                    return deltas[0] / (g + 1)
                if g == 0:
                    return max(deltas[:n])
                res = min(max(deltas[n - 1] / (x + 1), dp(n - 1, g - x)) for x in range(g + 1))
                return res

            return dp(D, k)

        # return fxr_knapsack()
        return fun4LeetCode_bisect()


sl = Solution()
print(sl.minmaxGasDist(stations=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=9))
print(sl.minmaxGasDist(stations=[23, 24, 36, 39, 46, 56, 57, 65, 84, 98], k=1))
