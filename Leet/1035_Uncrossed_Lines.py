"""
✅ GOOD DP (LCS)
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
Day 7: DP on String

Lookback
- Use defaultdict rather 2D array, is more convenient!
- re-state problem to reduce it to familar problems
"""


from collections import defaultdict
from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        def lee215():
            """
            Runtime: 280 ms, faster than 41.29% of Python3 online submissions for Uncrossed Lines.

            Same as classic DP problem LCS, the question maker cleverly deformed it.
            """
            T, m, n = defaultdict(int), len(A), len(B)
            for i in range(m):
                for j in range(n):
                    if A[i] == B[j]:
                        T[i, j] = T[i - 1, j - 1] + 1
                    else:
                        T[i, j] = max(T[i - 1, j], T[i, j - 1])
            return T[m - 1, n - 1]

        return lee215()


sl = Solution()
print(sl.maxUncrossedLines([1, 4, 2], [1, 2, 4]))
