"""
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        """
        Runtime: 32 ms, faster than 57.59% of Python3 online submissions for N-th Tribonacci Number.

        """
        F = {}

        def rec(i):
            if i in F:
                return F[i]
            if i < 3:
                # XXX: clean code fomr OS
                return 1 if i else 0
            ans = rec(i-1)+rec(i-2)+rec(i-3)
            F[i] = ans
            return ans
        return rec(n)


sl = Solution()
print(sl.tribonacci(n=4))
print(sl.tribonacci(n=25))
