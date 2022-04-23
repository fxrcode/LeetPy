"""
tag: medium
Lookback:
- simple 2ptr
"""

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        def fxr():
            """
            Runtime: 452 ms, faster than 95.66% of Python3 online submissions for Boats to Save People.

            """
            people.sort()
            i, j = 0, len(people) - 1
            ans = 0
            while i <= j:
                ans += 1
                if people[i] + people[j] <= limit:
                    i += 1
                j -= 1
            return ans
