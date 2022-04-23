"""
tag: Medium, Slide-window
Lookback:
- Don't use set for window, cause it may have multiple in window, only discard when freq = 0!
"""

from collections import Counter
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        def fxr():
            """
            Runtime: 1509 ms, faster than 13.31% of Python3 online submissions for Fruit Into Baskets.
            """
            l, r = 0, 0
            used = Counter()
            # BUG: used = set()
            mx = 0
            while r < len(fruits):
                c = fruits[r]
                r += 1
                used[c] += 1
                while len(used) > 2:
                    d = fruits[l]
                    l += 1
                    used[d] -= 1
                    if used[d] == 0:
                        used.pop(d)
                # max window with <= 2 used
                mx = max(mx, r - l)
            return mx

        return fxr()


sl = Solution()
# print(sl.totalFruit(fruits=[0, 1, 2, 2]))
# print(sl.totalFruit(fruits=[1, 2, 3, 2, 2]))
print(sl.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
