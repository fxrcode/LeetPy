"""
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
Day 8: DP on String
"""
from collections import defaultdict


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def labuladong():
            """
            # TODO: recursion, and I like his suffix indexing
            <详解最长公共子序列问题，秒杀三道动态规划题目> https://mp.weixin.qq.com/s/ZhPEchewfc03xWv9VP3msg
            """
            pass

        def fxr_lcs():
            """
            hat version LCS
            Runtime: 996 ms, faster than 39.22% of Python3 online submissions for Minimum ASCII Delete Sum for Two Strings.

            AC in 2: due to base case init.
            metacognition: My drawing 'saa','eat' DP table is quite helpful
                and lee215's 1035. Uncrossed Lines's defaultdict as DP table is helpful too
            """
            T, m, n = defaultdict(int), len(s1), len(s2)

            # XXX: careful on index (-1) for base case
            for i in range(m):
                T[i, -1] = T[i - 1, -1] + ord(s1[i])
            for j in range(n):
                T[-1, j] = T[-1, j - 1] + ord(s2[j])

            for i in range(m):
                for j in range(n):
                    if s1[i] == s2[j]:
                        T[i, j] = T[i - 1, j - 1]
                    else:
                        T[i, j] = min(
                            T[i - 1, j] + ord(s1[i]),
                            T[i, j - 1] + ord(s2[j]),
                        )
                        #   T[i-1, j-1] + ord(s1[i]) + ord(s2[j]))
            print(T)
            return T[m - 1, n - 1]

        return fxr_lcs()


sl = Solution()
print(sl.minimumDeleteSum(s1="sea", s2="eat"))
print(sl.minimumDeleteSum(s1="delete", s2="leet"))
