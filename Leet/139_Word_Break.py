"""
✅ GOOD Backtrack
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
Day 15: Memoization

tag: medium, DP, dfs (memo)
Lookback:
- Impl dfs w/ immutable state + return, so as to @cache. Don't use 9chap backtrack template, it's not Good for @cache.

Similar:
- 131. Palindrome Partitioning
"""

from functools import cache
from typing import List


class Solution:
    def wordBreak_os_backtrack(self, s: str, wordDict: List[str]) -> bool:
        """[summary]
        Runtime: 40 ms, faster than 65.14% of Python3 online submissions for Word Break.

        XXX: OS: wordbreak is like puzzle game. Analogy: puzzle <-> complete word, pieces <-> word dict.
        Top-down: When you start from complete puzzle and remove one valid piece at a time, until we reach empty.
            - why recursion, cuz we're asking the same question on smaller & smaller versions of given substring.
        Bottom-up: When we go from empty and use puzzle pieces to build up the final puzzle.

        T: as explained in 9chap, a word can be partitioned in n+1 slots, each slot can be cut or not cut, so O(2^n)
            eg. abcd => |a|b|c|d|
        """

        @cache
        def bt(start) -> bool:
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[s:end] in wd and bt(end):
                    return True
            return False

        wd = set(wordDict)
        return bt(0)

    def wordBreak_os_dp(self, s: str, wordDict: List[str]) -> bool:
        T = [False] * len(s) + 1
        T[0] = True
        wd = set(wordDict)

        for i in range(1, len(s) + 1):
            for j in range(i):
                if T[j] and s[j:i] in wd:
                    T[i] = True
                    break
        return T[len(s)]

    def wordBreak_DFS(self, s: str, wordDict: List[str]) -> bool:
        """[summary]
        TODO:dp. For dp problems, many times we go into iterative dp directly without even thinking about dfs. This is a great example showing that dfs is better than dp.
        DFS returns as soon as it finds one way to break the word while dp computes if each substring starting/ending at i is breakable.
        The test cases of this problem do not show it but it is shown in a similar problem Concatenated Words.
        https://leetcode.com/problems/word-break/discuss/43886/Evolve-from-brute-force-to-optimal-a-review-of-all-solutions
        """
