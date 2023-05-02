"""
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

date: 05012023
tag: Easy
Lookback:
"""

from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        def fxr():
            """
            Runtime: 43 ms, faster than 53.50% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
            T:O(N)
            """
            mn, mx, tot = float("inf"), 0, 0
            for s in salary:
                mn = min(mn, s)
                mx = max(mx, s)
                tot += s
            return (tot - mn - mx) / (len(salary) - 2)

        return fxr()


sl = Solution()
assert sl.average(salary=[4000, 3000, 1000, 2000]) == 2500
print(sl.average(salary=[1000, 2000, 3000]))
