"""
date: 0424023
tag: Easy, Heapq
Lookback:
[ ] TODO: counting sort
"""

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def lee215_heapq():
            h = [-x for x in stones]
            heapify(h)
            while len(h) > 1 and h[0] != 0:
                heappush(h, heappop(h) - heappop(h))
            return -h[0]

        def fxr():
            """
            Runtime: 52 ms, faster than 32.10% of Python3 online submissions for Last Stone Weight.

            T: O(nlogn)
            """
            mxheap = [-s for s in stones]
            heapify(mxheap)  # O(N)
            # for s in stones:
            #     heappush(mxheap, -s)
            while len(mxheap) >= 2:
                y = -heappop(mxheap)
                x = -heappop(mxheap)
                if x == y:
                    pass
                elif x != y:
                    heappush(mxheap, -(y - x))
            # BUG: return -mxheap[0]
            return -heappop(mxheap) if mxheap else 0

        return fxr()


sl = Solution()
print(sl.lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]))
assert sl.lastStoneWeight([2, 2]) == 0
