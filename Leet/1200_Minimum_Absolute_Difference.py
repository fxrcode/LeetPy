"""
Daily Challenge (Dec 20)

"""


from heapq import heapify, heappop
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        def os_counting_sort():
            # TODO
            pass

        def fxr():
            """
            Runtime: 392 ms, faster than 33.38% of Python3 online submissions for Minimum Absolute Difference.
            """
            arr.sort()
            ret = []
            pq = []
            for i in range(len(arr) - 1):
                pq.append((arr[i + 1] - arr[i], arr[i], arr[i + 1]))
            heapify(pq)
            mn = pq[0][0]
            while pq and pq[0][0] <= mn:
                d, a, b = heappop(pq)
                ret.append([a, b])
            return ret
