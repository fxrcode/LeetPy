"""
tag: Easy, DP,
takeaway:
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming
"""


from functools import cache


class Solution:
    def tribonacci(self, n: int) -> int:
        """
        Runtime: 32 ms, faster than 57.59% of Python3 online submissions for N-th Tribonacci Number.

        """

        @cache
        def rec(i):
            if i < 3:
                return 1 if i else 0
            ans = rec(i - 1) + rec(i - 2) + rec(i - 3)
            return ans

        return rec(n)


sl = Solution()
print(sl.tribonacci(n=4))
print(sl.tribonacci(n=25))
