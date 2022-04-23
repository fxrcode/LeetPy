"""
✅ GOOD Backtrack => DP
Daily Challenge (Jan 5)

tag: medium, DP, dfs (memo)
Lookback:
- @cache iff dfs w/ immutable state + return. Don't use 9chap backtrack template, it's not Good for @cache.
    * But how to write dfs w/ return? Ans: think about it as DP func! take prefix/suffix/subarray and return sub-solution!

Similar: 
- 139. Word Break
- 1849
"""

from functools import cache
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def linfq():
            """
            Runtime: 612 ms, faster than 99.40% of Python3 online submissions for Palindrome Partitioning.
            https://leetcode.com/problems/palindrome-partitioning/discuss/1667786/Python-Simple-Recursion-oror-Detailed-Explanation-oror-Easy-to-Understand
            T: O(N*2^N)
            """

            @cache
            def dfs(start):
                if start >= len(s):
                    return [[]]
                res = []
                for end in range(start + 1, len(s) + 1):
                    pre = s[start:end]
                    if pre == pre[::-1]:
                        for lls in dfs(end):
                            res.append([pre] + lls)
                return res

            return dfs(0)

        return linfq()

        def fxr():
            """
            XXX: Bad 9chap backtrack template, not easy to @cache
            Runtime: 1154 ms, faster than 5.76% of Python3 online submissions for Palindrome Partitioning.

            O(N*2^N)
            """
            L = len(s)

            @cache
            def ispalin(i, j):
                while i < j:
                    if s[i] != s[j]:
                        return False
                    i, j = i + 1, j - 1
                return True

            def bt(i, path, res):
                if i == L:
                    res.append(path[:])
                    return

                for j in range(i, L):
                    if ispalin(i, j):
                        path.append(s[i : j + 1])
                        bt(j + 1, path, res)
                        path.pop()

            res = []
            bt(0, [], res)
            return res


sl = Solution()
print(sl.partition("aab"))
