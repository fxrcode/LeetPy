"""
✅ GOOD Backtrack => DP
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

tag: easy, math, dfs
Lookback:
- Similar to 1774 Dessert, 131 Palindrome Partition.
- Great problem to learn how to convert from backtrack to memo dfs (DP):
    Ans: think in DP!

Flow-Up:
- given target time, return closest time you can get (inspired by 1774)
"""

from functools import cache
from itertools import product
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def stefan():
            """
            Runtime: 35 ms, faster than 81.98% of Python3 online submissions for Binary Watch.

            base-2 enumeration
            T: O(12*60)
            """
            return [f"{h}:{m:02d}" for h in range(12) for m in range(60) if (bin(h) + bin(m)).count("1") == turnedOn]

        def fxr():
            @cache
            def bt(left, hh, mm):
                """
                Runtime: 137 ms, faster than 5.04% of Python3 online submissions for Binary Watch.

                T: O(n*2^h*2^m) # h=4,m=6
                """
                if hh >= 12 or mm > 59:
                    return
                if left == 0:
                    res.add(f"{hh}:{mm:02d}")
                    return
                for h, m in product(range(4), range(6)):
                    if (1 << h) & hh == 0:
                        bt(left - 1, hh | (1 << h), mm)
                    if (1 << m) & mm == 0:
                        bt(left - 1, hh, (1 << m) | mm)

            res = set()
            bt(turnedOn, 0, 0)
            return sorted(list(res))

        # return fxr()
        return stefan()


sl = Solution()
print(sl.readBinaryWatch(2))
