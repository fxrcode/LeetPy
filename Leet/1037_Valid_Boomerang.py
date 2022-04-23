"""
tag: Easy, Math
Lookback: 
- We can reuse the conclusion and prove in 812. Largest Triangle Area
"""

from typing import List


class Solution:
    def isBoomerang(self, p: List[List[int]]) -> bool:
        def rock():
            # Runtime: 39 ms, faster than 68.81% of Python3 online submissions for Valid Boomerang.
            return (p[0][0] - p[1][0]) * (p[0][1] - p[2][1]) != (p[0][0] - p[2][0]) * (p[0][1] - p[1][1])
