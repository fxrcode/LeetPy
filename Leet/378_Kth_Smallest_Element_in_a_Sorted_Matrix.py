"""
✅ GOOD bisect (k-th min/max/freq) in set
✅ GOOD heapq (merge N sorted list)
Tag: Medium, heapq, bisect, array
Lookback:
- not familiar w/ merge N sorted list
- didn't fully learned from 668
Similar:
- heapq: 373, 1057
- bisect: 668
- countLessOrEqual => 240
"""

from heapq import heappop, heappush
from typing import List

from numpy import mat


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def hiepit_heapq():
            """
            Runtime: 210 ms, faster than 82.23% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.

            reminds me 1057. Campus Bike: merge N sorted list
            T: O(X + KlogX), X=min(k,m)
            """
            m = len(matrix)
            minheap = []
            for r in range(min(k, m)):
                heappush(minheap, (matrix[r][0], r, 0))
            ans = None
            for i in range(k):
                ans, r, c = heappop(minheap)
                if c + 1 < m:
                    heappush(minheap, (matrix[r][c + 1], r, c + 1))
            return ans

        def hiepit_bisect():
            """
            Runtime: 282 ms, faster than 44.64% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.

            https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1322101/C%2B%2BJavaPython-MaxHeap-MinHeap-Binary-Search-Picture-Explain-Clean-and-Concise
            T: O((M+N) * logD). # D=max-min
            """

            def count_le(x):
                cnt = 0
                c = m - 1
                for r in range(m):
                    while c >= 0 and matrix[r][c] > x:
                        c -= 1
                    cnt += c + 1
                return cnt

            m = len(matrix)
            l, r = matrix[0][0], matrix[-1][-1]
            while l < r:
                mid = (l + r) // 2
                if count_le(mid) >= k:
                    r = mid
                else:
                    l = mid + 1
            return l

        return hiepit_bisect()


sl = Solution()
print(sl.kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8))
print(sl.kthSmallest(matrix=[[1, 5], [2, 7]], k=3))
