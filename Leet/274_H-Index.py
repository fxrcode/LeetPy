"""
✅ GOOD Sort
tag: medium, sort
Lookback:
- draw a plot to find inner property!
- when range limit => use bucket sort (optimize via Discretization)
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def os_sort():
            """
            Runtime: 36 ms, faster than 94.71% of Python3 online submissions for H-Index.

            T: O(NlogN)
            """
            citations.sort(reverse=True)
            h = 0
            for i, c in enumerate(citations):
                if c > i:
                    h += 1
                else:
                    break
            return h

        return os_sort()


sl = Solution()
print(sl.hIndex(citations=[3, 0, 6, 1, 5]))
print(sl.hIndex(citations=[1, 3, 1]))
