"""
date: 02212023
tag: Medium, bisect
lookback:
- bad in simple feasible logic
"""

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def fxr_bisect():
            def feasible(capacity) -> bool:
                """
                https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/769698/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.
                zhijun_liao feasible is more cleaner than mine
                """
                d = 1
                tot = 0
                for w in weights:
                    tot += w
                    if tot > capacity:  # too heavy, wait for the next day
                        tot = w
                        d += 1
                        if d > days:  # cannot ship within D days
                            return False
                return True

            def feasible_fxr(x):
                c = 0
                d = 1
                for w in weights:
                    if c + w > x:
                        c = w
                        d += 1
                    else:
                        c += w
                    if d > days:
                        return False
                if d <= days:
                    return True
                return False

            l, r = max(weights), sum(weights) + 1
            while l < r:
                m = (l + r) // 2
                if feasible(m):
                    r = m
                else:
                    l = m + 1
            return l

        return fxr_bisect()


sl = Solution()

print(sl.shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))
print(sl.shipWithinDays(weights=[3, 2, 2, 4, 1, 4], days=3))
