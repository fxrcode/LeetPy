'''
Daily Challenge (Feb 4)
tag: Medium, Hash, Presum

Lookback:
- transform problem to ease by make 0=>-1. Equal #0/1 in subarr === sum = 0!
- to get max len of this subarr, we need to mark 1st occur index of each presum
    if presum[j] - presum[i-1] = 0, then we update maxlen
'''

from collections import defaultdict
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        def fxr_presum():
            """
            Runtime: 888 ms, faster than 67.30% of Python3 online submissions for Contiguous Array.

            T: O(N)
            M: O(N)

            XXX: AC @4th!
            """
            vi = {0: -1}
            P = 0
            mx = 0
            for i, v in enumerate(nums):
                P += v if v == 1 else -1
                if P in vi:
                    mx = max(mx, i - vi[P])
                else:
                    vi[P] = i
            return mx

        return fxr_presum()


sl = Solution()
# nums = [0, 1, 0]
# nums = [0, 1]
# nums = [0, 1, 0, 1]
nums = [0, 1, 1]
print(sl.findMaxLength(nums))
