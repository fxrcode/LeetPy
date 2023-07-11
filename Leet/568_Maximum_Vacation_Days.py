"""
💡✅ GOOD Backtrack
Weekly Special (Jan W1)

Lookback:
- It's hard due to lenghthy description, actually, it's easy in logic & impl!
- Handy max([], default=0)
"""

from functools import cache
from typing import List


class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        def jinjiren_dfs():
            """
            Runtime: 1969 ms, faster than 79.02% of Python3 online submissions for Maximum Vacation Days.

            REF: https://leetcode.com/problems/maximum-vacation-days/discuss/267874/Python3-top-down-%2B-bottom-up-DP-solutions-with-explanation.

            T: O(NK)
            """
            N, K = len(days), len(days[0])
            CanFly = [
                [i for i, can_fly in enumerate(city) if can_fly] for city in flights
            ]

            print(CanFly)

            @cache
            def dfs(week, city):
                """
                !because there is no state change, we can use memoization

                return the number of vacation which can be traken starting from city and week
                Top-down dfs DP, be like tear piece-by-piece from full puzzle
                """
                if week == K:
                    return 0

                # opt1: stay in city @week, and recursive call: starting from same city @week+1
                stay = days[city][week] + dfs(week + 1, city)

                # opt2: pick the max vacation days can get from all other city that I can fly to from city @week
                #   since fly cost no day, so we can fly to other and play!
                #   gotcha, there might be no others! So default 0
                fly = max(
                    (
                        days[other][week] + dfs(week + 1, other)
                        for other in CanFly[city]
                    ),
                    default=0,
                )
                return max(stay, fly)

            return dfs(0, 0)

        return jinjiren_dfs()

        def fxr_mrcheung():
            """
            https://www.youtube.com/watch?v=EbJaBD0FpKY

            TLE: 39 / 57 test cases passed.
            """
            ans = 0
            N, K = len(flights), len(days[0])
            AL = {i: set([i]) for i in range(N)}
            for i in range(N):
                for j in range(N):
                    if flights[i][j]:
                        AL[i].add(j)

            @cache
            def dfs(week, city, vacations):
                nonlocal ans
                if week == K:
                    ans = max(ans, vacations)
                    return
                for other in AL[city]:
                    dfs(week + 1, other, vacations + days[other][week])

            dfs(0, 0, 0)
            return ans


sl = Solution()
print(
    sl.maxVacationDays(
        flights=[[0, 1, 1], [1, 0, 1], [1, 1, 0]],
        days=[[1, 3, 1], [6, 0, 3], [3, 3, 3]],
    )
)
