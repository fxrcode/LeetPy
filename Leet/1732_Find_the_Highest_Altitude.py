"""
tag: Easy, presum
Lookback:
- similar to 1352
"""

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        def fxr():
            """
            Runtime: 37 ms, faster than 81.63% of Python3 online submissions for Find the Highest Altitude.

            """
            pre = 0
            ans = 0
            for n in gain:
                pre += n
                ans = max(ans, pre)
            return ans

        return fxr()


sl = Solution()
print(sl.largestAltitude(gain=[-5, 1, 5, 0, -7]))
print(sl.largestAltitude(gain=[-4, -3, -2, -1, 4, 3, 2]))
