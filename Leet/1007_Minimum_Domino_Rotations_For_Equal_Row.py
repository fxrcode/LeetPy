"""
✅ GOOD Logic
Daily Challenge (Mar 20, 2022)
tag: medium, Google, logic, Greedy
Lookback:
- only tried eg for 1min, then spent 30min on FSM DP (like stock) but failed to find relation.
- MUST FULLY understand the problem before coding!
"""

from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def lee215():
            def _sol1():
                """
                Runtime: 1424 ms, faster than 55.54% of Python3 online submissions for Minimum Domino Rotations For Equal Row.

                """
                for x in [tops[0], bottoms[0]]:
                    if all(x in d for d in zip(tops, bottoms)):
                        return len(tops) - max(tops.count(x), bottoms.count(x))
                return -1

            return _sol1()

        return lee215()


sl = Solution()
print(sl.minDominoRotations(tops=[2, 1, 2, 4, 2, 2], bottoms=[5, 2, 6, 2, 3, 2]))
print(sl.minDominoRotations(tops=[3, 5, 1, 2, 3], bottoms=[3, 6, 3, 3, 4]))
