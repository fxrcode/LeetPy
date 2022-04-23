"""
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        # from neetcode
        # Runtime: 24 ms, faster than 97.34% of Python3 online submissions for Ugly Number.
        if n <= 0:
            return False

        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        return n == 1


sl = Solution()
print(sl.isUgly(22))
print(sl.isUgly(15))
print(sl.isUgly(14))
