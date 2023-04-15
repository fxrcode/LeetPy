"""
✅ GOOD DP (Subsequence - LPS)
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming

Day 12: DP on String
date: 04132023
tag: Medium, DP
"""
from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def hiepit_topdown():
            """
            Runtime: 944 ms, faster than 91.01% of Python3 online submissions for Longest Palindromic Subsequence.

            T: O(n^2), M: O(n^2)
            """
            n = len(s)

            @cache
            def dp(l, r):
                if l > r:
                    return 0
                if l == r:
                    return 1
                if s[l] == s[r]:
                    return dp(l + 1, r - 1) + 2
                return max(dp(l, r - 1), dp(l + 1, r))

                # XXX: why considering these 2? because that's subproblem of current problem (l,r)
                # BUG: don't add 1, because we're directly checking sub-problem!
                # return max(dp(l, r-1), dp(l+1, r))+1

            return dp(0, n - 1)

        def hiepit_bottomup():
            """
            https://leetcode.com/problems/longest-palindromic-subsequence/discuss/1468396/C%2B%2BPython-2-solutions%3A-Top-down-DP-Bottom-up-DP-O(N)-Space-Clean-and-Concise
            TODO:
            """
            pass
