"""
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
Day 13: Min/Max Path Sum

Metacognition:
* Always think about brute force first! Be asymmetrical!
"""


from collections import defaultdict
from typing import List


class Solution:
    def longestLine(self, A: List[List[int]]) -> int:
        def fxr():
            """
            Runtime: 536 ms, faster than 53.17% of Python3 online submissions for Longest Line of Consecutive One in Matrix.

            REF: https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/discuss/102275/Python-Simple-with-Explanation
            metacognition:
            * seems simple if only horizontal, vertial, and diagonal.
            * ~~to handle anti-diagonal, will do extra DP for it.~~

            Lookback: OS, always do a concrete case walk through, then re-think my thought,
                the anti-diagonal can be update along with H/V/D, so a single mat traverse is suffice.
            """
            m, n = len(A), len(A[0])
            mx = 0
            T = defaultdict(lambda: [0, 0, 0, 0])

            # easier matrix traversal
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val:
                        T[r, c][0] = T[r, c - 1][0] + 1
                        T[r, c][1] = T[r - 1, c][1] + 1
                        T[r, c][2] = T[r - 1, c - 1][2] + 1
                        T[r, c][3] = T[r - 1, c + 1][3] + 1
                        mx = max(mx, max(T[r, c]))
            return mx
