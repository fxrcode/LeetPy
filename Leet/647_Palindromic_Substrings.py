"""
✅ GOOD Subarray DP (outer loop len, inner loop (lo,hi) boundary)
Tag: Medium, DP, 2ptr, string
Lookback:
- basic skill of palindrome

https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
Day 11: DP on String

https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions
"""
from collections import defaultdict


class Solution:
    def countSubstrings(self, s: str) -> int:
        def center_expand():
            """
            Runtime: 155 ms, faster than 66.10% of Python3 online submissions for Palindromic Substrings.
            T: O(N^2)
            """

            def expand(l, r):
                cnt = 0
                while l >= 0 and r < n and s[l] == s[r]:
                    l, r = l - 1, r + 1
                    cnt += 1
                return cnt

            ans = 0
            n = len(s)
            for i in range(len(s)):
                ans += expand(i, i)
                ans += expand(i, i + 1)
            return ans

        def substring_dp():
            """
            Runtime: 592 ms, faster than 15.02% of Python3 online submissions for Palindromic Substrings.

            REF: OS substring DP loop len, then inner loop substr
            """
            n = len(s)
            ans = 0
            F = defaultdict(bool)
            for i in range(n):
                # base case for odd (len=1)
                F[(i, i)] = True
                ans += 1
                # base case for even (len=2)
                if i + 1 < n and s[i] == s[i + 1]:
                    F[(i, i + 1)] = True
                    ans += 1

            # XXX: python gotcha, the scope of var inside loop can still be access outside.
            #       it's a design decision, and usage as in for/else.
            #       one way is to wrap things inside a func.
            i = 0
            for sz in range(3, n + 1):
                # BUG: Python Gotcha,if you write in one-line,
                # i, j = 0, i+sz-1
                i, j = 0, sz - 1
                # print('len', sz, i, j)
                while j < n:
                    F[(i, j)] = F[(i + 1, j - 1)] and s[i] == s[j]
                    ans += F[(i, j)]
                    i, j = i + 1, j + 1
            return ans

        def fxr_bf():
            """
            TLE
            T: O(N^3), since s.length ~ 1000, so max = 10^9!
            """

            def is_pa(i, j):
                while i <= j:
                    if s[i] != s[j]:
                        return False
                    i, j = i + 1, j - 1
                return True

            count = 0
            n = len(s)
            for i in range(n):
                for j in range(i, n):
                    if is_pa(i, j):
                        count += 1
            return count

        # return fxr_bf()
        # return substring_dp()
        return center_expand()


sl = Solution()
# print(sl.countSubstrings('abc'))
# print(sl.countSubstrings('aaa'))
print(sl.countSubstrings("aaaaa"))
