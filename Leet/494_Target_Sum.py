"""
https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1389/
Explore Queue-Stack: DFS

tag: DP, dfs
Lookback:
- Optimize from Backtrack => DP (top-down DP)
"""

import timeit
from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def findTargetSumWays_DP(self, nums: List[int], target: int) -> int:
        """
        Runtime: 321 ms, faster than 75.13% of Python3 online submissions for Target Sum.

        Re-read labuladong book: CH 2.19: What's relation of Backtracking & DP?
        Q: How to find overlapping subproblems? A: check recursion calls, and find duplicate STATES!
        """

        @cache
        def dp(i, s) -> int:
            """[summary]
            Labuladong Ch 2.19
            (i, res) is the state, and we found overlapping subproblems, `say nums[i] = 0`
            memo is map {state -> result}
            """
            # base case
            if i == len(nums):
                if s == 0:
                    return 1
                return 0

            return dp(i + 1, s - nums[i]) + dp(i + 1, s + nums[i])

        # driver code
        if not nums:
            return 0
        return dp(0, target)

    def findTargetSumWays_lee215_BFS(self, nums: List[int], target: int) -> int:
        """[summary]
        Your runtime beats 77.58 % of python3 submissions.

        https://leetcode.com/problems/target-sum/discuss/97439/JavaPython-Easily-Understood
        Use 2 dict, and swap after finish current level.
        T: O(2^N)
        """
        count = defaultdict(int)  # map {sum : #ways}
        count[0] = 1
        # every number is a level, can +x or -x from upper level
        for x in nums:
            step = defaultdict(int)
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step

        return count[target]

    def findTargetSumWays_fxr1_TLE(self, nums: List[int], target: int) -> int:
        """[summary]
        1st try on 09162021
        TLE: 46 / 139 test cases passed. Last executed input: [33,36,38,40,25,49,1,8,50,13,41,50,29,27,18,25,37,8,0,48], 0
        T: O(2^N)
        """

        def backtrack(i, res, ans) -> None:
            if i == len(nums):
                if res == 0:
                    ans[0] += 1
                return
            for sgn in [+1, -1]:
                backtrack(i + 1, res - sgn * nums[i], ans)

        ans = [0]
        backtrack(0, target, ans)
        return ans[0]


"""
# TODO: DP.
#   Refer to great summary post: https://leetcode.com/problems/target-sum/discuss/455024/DP-IS-EASY!-5-Steps-to-Think-Through-DP-Questions.
"""

sl = Solution()

sl.findTargetSumWays_lee215_BFS([1, 2, 1, 3], 1)

print(sl.findTargetSumWays_DP(nums=[1], target=1))
# print(sl.findTargetSumWays_fxr2(nums=[2, 1], target=1))
print(sl.findTargetSumWays_DP(nums=[1, 1, 1, 1, 1], target=3))
stmt_tle = """
sl.findTargetSumWays_fxr1_TLE(nums=[33, 36, 38, 40, 25, 49, 1, 8, 50, 13, 41, 50, 29, 27, 18, 25, 37, 8, 0, 48], target=0)
"""
stmt_lee = """
sl.findTargetSumWays_lee215_BFS(nums=[33, 36, 38, 40, 25, 49, 1, 8, 50, 13, 41, 50, 29, 27, 18, 25, 37, 8, 0, 48], target=0)
"""
stmt_dp = """
sl.findTargetSumWays_DP(nums=[33, 36, 38, 40, 25, 49, 1, 8, 50, 13, 41, 50, 29, 27, 18, 25, 37, 8, 0, 48], target=0)
"""
setup_sl = "from __main__ import Solution; sl = Solution()"

print("TLE Backtrack", timeit.timeit(stmt=stmt_tle, setup=setup_sl, number=3))
print("BFS", timeit.timeit(stmt=stmt_lee, setup=setup_sl, number=3))
print("memo DP", timeit.timeit(stmt=stmt_dp, setup=setup_sl, number=3))
"""

TLE Backtrack 1.6064356539936853
BFS 0.0073862990029738285
memo DP 0.01147795699944254
"""
