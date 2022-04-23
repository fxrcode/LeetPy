"""
tag: easy, hash
Lookback:

"""

from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        def fxr():
            # Runtime: 56 ms, faster than 95.16% of Python3 online submissions for Find Lucky Integer in an Array.
            cnt = Counter(arr)
            ans_n, ans_f = None, 0
            for n, f in cnt.items():
                if n == f and ans_f <= f:
                    ans_f = f
                    ans_n = n
            return ans_n if ans_n else -1

        return fxr()


sl = Solution()
print(sl.findLucky(arr=[2, 2, 3, 4]))
print(sl.findLucky(arr=[1, 2, 2, 3, 3, 3]))
assert sl.findLucky(arr=[2, 2, 2, 3, 3]) == -1
