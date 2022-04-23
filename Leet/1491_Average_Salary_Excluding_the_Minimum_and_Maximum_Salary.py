'''
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

Lookback:
'''

from typing import List


class Solution:

    def average(self, salary: List[int]) -> float:

        def fxr():
            """
            Runtime: 43 ms, faster than 53.50% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
            T:O(N)
            """
            mn, mx, tot = float('inf'), 0, 0
            for s in salary:
                tot += s
                mn = min(mn, s)
                mx = max(mx, s)
            return (tot - mn - mx) / (len(salary) - 2)
