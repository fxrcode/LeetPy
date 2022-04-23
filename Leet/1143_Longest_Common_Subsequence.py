"""
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
tag: DP, dfs
Lookback:
- LCS/LIS/LPS/TSP/Knapssack/Edit Dist/Coin Change classic DP

Similar LCS
516. Longest Palindromic Subsequence
718. Maximum Length of Repeated Subarray
1035. Uncrossed Lines
1062. Longest Repeating Substring (Premium).
1092. Shortest Common Supersequence and Solution
1312. Minimum Insertion Steps to Make a String Palindrome
1458. Max Dot Product of Two Subsequences

"""


from functools import cache


class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        def fxr():
            """
            Runtime: 1346 ms, faster than 14.16% of Python3 online submissions for Longest Common Subsequence.

            T: O(mn)
            """

            @cache
            def dp(i, j):
                if i == len(s1) or j == len(s2):
                    return 0
                elif s1[i] == s2[j]:
                    return 1 + dp(i + 1, j + 1)
                else:
                    return max(dp(i + 1, j), dp(i, j + 1))

            return dp(0, 0)

        return fxr()

        def labuladong():
            """
            Runtime: 384 ms, faster than 85.36% of Python3 online submissions for Longest Common Subsequence.

            T: O(mn)
            """
            m, n = len(s1), len(s2)
            T = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if s1[i - 1] == s2[j - 1]:
                        T[i][j] = T[i - 1][j - 1] + 1
                    else:
                        T[i][j] = max(T[i - 1][j], T[i][j - 1])
            return T[m][n]


sl = Solution()
print(sl.longestCommonSubsequence(s1="abcde", s2="ace"))
print(sl.longestCommonSubsequence(s1="babcde", s2="ace"))
