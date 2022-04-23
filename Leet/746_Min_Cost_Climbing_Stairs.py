"""

https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming

NOTE: OS: This is a good intro of DP, we can find 2 properties of the problem: find min/max solution; we have to make decisions that may vary depends on decisions we made previously.
    There're 2 type DP:
        1. Bottom-Up (tabulation, starts from base case to top)
        2. Top-down (recursion + memo, starts at top and works its way down to base cases.)

NOTE: Closing Notes
If you're new to dynamic programming, hopefully you learned something from this article. Please post any questions you may have in the comment section below. For additional practice, here's a list of similar dynamic programming questions that are good for beginners.
* 70. Climbing Stairs (Easy)
* 198. House Robber (Medium)
* 256. Paint House (Medium)
* 509. Fibonacci Number (Easy)
* 931. Minimum Falling Path Sum (Medium)
"""


from functools import cache
from typing import List


class Solution:
    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        @cache
        def reach(stair):
            """
            Runtime: 72 ms, faster than 26.24% of Python3 online submissions
            XXX: still confusing on the meaning of recursion func, cuz it's tricky to handle top stair.
                OS: "we're not counting the cost of step 4 yet since we are only talking about reaching the step right now"
            """
            if stair < 2:
                return 0
            j1 = reach(stair-1) + cost[stair-1]
            j2 = reach(stair-2) + cost[stair-2]
            return min(j1, j2)

        return reach(len(cost))

    def minCostClimbingStairs0(self, cost: List[int]) -> int:
        F = {}

        def rec(i):
            """
            Runtime: 133 ms, faster than 5.39% of Python3 online submissions for Min Cost Climbing Stairs.

            XXX: OS shows the example clearly, so the index is actually straightforward
            """
            if i < 2:
                return 0
            one_step = rec(i-1) + cost[i-1]
            two_step = rec(i-2) + cost[i-2]
            ans = min(one_step, two_step)
            return ans

        return rec(len(cost))
        '''
        XXX: lookback: why the indexing is diffcult for me? Because I lack to analysis before coding!
            do a thorough concrete example study as OS, then it's straightford indexing!
        def rec(i):
            """
            Runtime: 93 ms, faster than 21.43% of Python3 online submissions for Min Cost Climbing Stairs.

            AC in 1.
            XXX: but I'm always confuesd on indexing...
            XXX: rec(i) means the minimum cost to reach stair i
            """
            if i in F:
                return F[i]
            if i < 3:
                return 0

            # XXX: to get to i, we can jump 1 step from i-1, or 2 steps from i-2.
            # XXX: due to cost is 0-based, and actual 0-th step is 0, so I do the shift: ith cost-> cost[i-1]
            ans = min(rec(i-1)+cost[i-2], rec(i-2)+cost[i-3])
            F[i] = ans
            return ans

        return rec(len(cost)+1)
        '''


sl = Solution()
print(sl.minCostClimbingStairs(cost=[10, 15, 20]))
print(sl.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
