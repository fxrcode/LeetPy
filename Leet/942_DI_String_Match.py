"""
✅ GOOD Greedy
Tag: Easy, 2ptr, Logic
Lookback:
- understand problem by walk through given eg, rather play w/ random str by yourself, cuz they might not be valid.
Similar:
- follow up: 484 (lexical order)
"""

from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        def os_greedy():
            """
            Runtime: 72 ms, faster than 75.36% of Python3 online submissions for DI String Match.

            """
            n = len(s)
            lo, hi = 0, n
            res = []
            for c in s:
                if c == "I":
                    res.append(lo)
                    lo += 1
                else:
                    res.append(hi)
                    hi -= 1
            return res + [lo]

        return os_greedy()


sl = Solution()
print(sl.diStringMatch(s="IDID"))
print(sl.diStringMatch(s="III"))
print(sl.diStringMatch(s="DDI"))
