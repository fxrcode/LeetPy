"""
✅ GOOD Sort
Tag: Medium, Sort
Lookback:
- draw a plot to find inner property!
- when range limit => use bucket sort (optimize via Discretization)
- usage: #1608
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def os_sort():
            """
            Runtime: 48 ms, faster than 59.68% of Python3 online submissions for H-Index.

            T: O(NlogN)
            """
            citations.sort(reverse=True)
            i = 0
            while i < len(citations) and citations[i] > i:
                i += 1
            # now we got i paper has citations greater or equal to i.
            return i

        return os_sort()


sl = Solution()
print(sl.hIndex(citations=[3, 0, 6, 1, 5]))
print(sl.hIndex(citations=[1, 3, 1]))
