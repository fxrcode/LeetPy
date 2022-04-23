"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
from functools import cache


class Solution:
    def climbStairs1(self, n: int) -> int:
        # Your runtime beats 16.86 % of python3 submissions.
        @cache
        def recur(stair):
            if stair <= 2:
                return stair
            return recur(stair-2) + recur(stair-1)
        return recur(n)

    def climbStairs0(self, n: int) -> int:
        """
        Runtime: 33 ms, faster than 47.72% of Python3 online submissions for Climbing Stairs.

        https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1662/
        """
        F = {}

        def recur(n) -> int:
            if n in F:
                return F[n]
            if n < 4:
                result = n
            else:
                result = recur(n-1)+recur(n-2)
            F[n] = result
            return result

        return recur(n)


sl = Solution()
print(sl.climbStairs(10))
