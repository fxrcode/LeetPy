"""
tag: Hard, DP
Lookback:
- reduce new problem to classic problem


Similar Problems:
72. Edit Distance
516. Longest Palindromic Subsequence
"""


from functools import cache


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def fxr_lps():
            """
            Runtime: 666 ms, faster than 55.05% of Python3 online submissions for Valid Palindrome III.

            """

            @cache
            def dp(i, j):
                if i > j:
                    return 0
                elif i == j:
                    return 1
                if s[i] == s[j]:
                    return dp(i + 1, j - 1) + 2
                else:
                    return max(dp(i + 1, j), dp(i, j - 1))

            return dp(0, len(s) - 1) >= len(s) - k

        return fxr_lps()


sl = Solution()
print(sl.isValidPalindrome(s="abcdeca", k=2))
print(sl.isValidPalindrome(s="abbababa", k=1))
