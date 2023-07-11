"""
✅ GOOD Greedy (logic)
tag: easy, skills, math
Lookback:
- easy?! yes. It's easy, but still needs brain.
- 5 has larger possibility to be used: 10->5, 20-> 5+10 or 5+5+5. 
"""

from collections import defaultdict
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        def lee215():
            # Runtime: 1299 ms, faster than 26.47% of Python3 online submissions for Lemonade Change.
            five = ten = 0
            for b in bills:
                if b == 5:
                    five += 1
                elif b == 10:
                    five, ten = five - 1, ten + 1
                elif ten > 0:
                    five, ten = five - 1, ten - 1
                else:
                    five -= 3
                if five < 0:
                    return False
            return True

        return lee215()

        def fxr():
            """
            Runtime: 1257 ms, faster than 30.43% of Python3 online submissions for Lemonade Change.

            XXX: 3*WA ?!
            """
            cnt = defaultdict(int)
            for i, b in enumerate(bills):
                if b == 5:
                    cnt[5] += 1
                elif b == 10:
                    if cnt[5] > 0:
                        cnt[5] -= 1
                        cnt[10] += 1
                    else:
                        return False
                else:
                    if cnt[5] > 0 and cnt[10] > 0:
                        cnt[5] -= 1
                        cnt[10] -= 1
                        cnt[20] += 1
                    elif cnt[5] >= 3:
                        cnt[5] -= 3
                    else:
                        return False
            return True


sl = Solution()
# assert sl.lemonadeChange(bills=[5, 5, 5, 10, 20]) == True
# assert sl.lemonadeChange(bills=[5, 5, 10, 10, 20]) == False
assert (
    sl.lemonadeChange([5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5])
    == True
)
assert sl.lemonadeChange([5, 5, 5, 5, 20, 20, 5, 5, 20, 5]) == False
