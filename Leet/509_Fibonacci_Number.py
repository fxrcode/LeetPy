"""
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
"""
from functools import cache


class Solution:
    @cache
    def fib1(self, n: int) -> int:
        # Runtime: 24 ms, faster than 95.76% of Python3 online submissions for Fibonacci Number.
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    def fib0(self, n: int) -> int:
        """[summary]
        Your runtime beats 66.60 % of python3 submissions.
        https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1495/
        """
        F = {}

        def recur(n) -> int:
            if n in F:
                return F[n]
            if n < 2:
                result = n
            else:
                result = recur(n - 1) + recur(n - 2)
            F[n] = result
            return result

        return recur(n)


sl = Solution()
print(sl.fib(10))
