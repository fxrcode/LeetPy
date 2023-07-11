"""
tag: hard, dp, bisect, doordash
Lookback:
- zip & sort is handy
"""

from bisect import bisect_left
from functools import cache
from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        def hiepit_dp():
            """
            Runtime: 540 ms, faster than 94.64% of Python3 online submissions for Maximum Profit in Job Scheduling.

            https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/1430983/Python-From-Brute-Force-to-DP-and-Binary-Search-Clean-and-Concise
            """
            n = len(startTime)
            jobs = sorted(zip(startTime, endTime, profit))
            start = [jobs[i][0] for i in range(n)]

            @cache
            def dp(i):
                if i == n:
                    return 0
                ans = dp(i + 1)
                nxt = bisect_left(start, jobs[i][1])
                ans = max(ans, dp(nxt) + jobs[i][2])
                return ans

            return dp(0)

        return hiepit_dp()


sl = Solution()
print(
    sl.jobScheduling(
        startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]
    )
)
