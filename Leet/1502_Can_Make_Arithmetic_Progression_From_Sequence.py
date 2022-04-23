"""
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

tag: easy, math
Lookback:
- re-state problem!
"""


from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        def lenchen1112(A):
            """
            Runtime: 199 ms, faster than 5.39% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.

            """
            gap = (max(A) - min(A)) / (len(A) - 1)
            if gap == 0:
                return True
            s = set(n - min(A) for n in A)
            return len(s) == len(A) and all(diff % gap == 0 for diff in s)

        def rock_sort(A):
            A.sort()
            return all(A[i - 2] - A[i - 1] == A[i - 1] - A[i] for i in range(2, len(arr)))
