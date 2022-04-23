"""
tag: easy, math
Lookback:
- need speed-up
"""
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        def lee215():
            return range(1 - n, n, 2)

        return lee215()

        def fxr():
            # Runtime: 26 ms, faster than 98.56% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
            res = []
            # 4//2 = 2: [1,2] => [-1,-2]
            # 5//2 = 2: [1,2] => [-1,-2]+[0]
            for i in range(1, n // 2 + 1):
                res.append(i)
                res.append(-i)
            if n % 2:
                res.append(0)
            return res

        return fxr()


sl = Solution()
p = lambda x: print(list(x))
p(sl.sumZero(5))
p(sl.sumZero(7))
p(sl.sumZero(1))
