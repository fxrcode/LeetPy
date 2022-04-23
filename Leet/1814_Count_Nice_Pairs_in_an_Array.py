"""
tag: medium
Lookback:
- update res then update counter to prevent double count
- int('0021') => 21
"""

from collections import Counter
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def fxr():
            """
            Runtime: 883 ms, faster than 71.57% of Python3 online submissions for Count Nice Pairs in an Array.

            """
            freq = Counter()
            res = 0
            for a in nums:
                b = int(str(a)[::-1])
                res += freq[a - b]
                freq[a - b] += 1
            return res % (10**9 + 7)

        return fxr()


sl = Solution()
print(sl.countNicePairs(nums=[42, 11, 1, 97]))
print(sl.countNicePairs(nums=[13, 10, 35, 24, 76]))
