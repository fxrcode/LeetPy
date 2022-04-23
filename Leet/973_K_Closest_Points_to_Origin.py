"""
✅ GOOD Quick-select (recursion vs binary search)
tag: medium, bisect, recursion
Lookback:
- Lucky, I revisited Mar 21, 2022, and found my AC impl got TLE (forever loop), then I found I didn't fully understood lomuto or binary-search template!
    * eg. A = [3,3,3,3,3,3]. in lomuto, if I use if dist(A[j]) < pdist, then no change, and returned 0

Daily Challenge (Dec 26)

[ ] REDO
"""

from heapq import heappop, heappush
from random import randint
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = lambda x: x[0] ** 2 + x[1] ** 2

        def lomuto(A, l, r):
            d = randint(l, r)  # random int in [l...r]
            A[d], A[r] = A[r], A[d]
            pdist = dist(A[r])
            i = l - 1
            for j in range(l, r):
                """
                # if A[j] <= pivot:  `same as Wiki, use <=`
                invariant
                +------+---+---+
                |   <= | > |  p|
                +------+---+---+
                |     ^|   |^  |
                |     i|   |j  |
                +------+---+---+
                """
                if dist(A[j]) <= pdist:
                    i += 1
                    A[i], A[j] = A[j], A[i]
            A[i + 1], A[r] = A[r], A[i + 1]
            return i + 1

        def qselect():
            """
            Runtime: 1259 ms, faster than 32.70% of Python3 online submissions for K Closest Points to Origin.

            XXX: thanks to Mar, 2022 new test cases (many equal points, needs careful impl to prevent forever loop!)
            """
            l, r, p = 0, len(points) - 1, 0
            while l < r:
                p = lomuto(points, l, r)
                if p == k - 1:
                    break
                elif p > k - 1:
                    r = p - 1
                else:
                    l = p + 1
            return points[:k]

        return qselect()

        def qselect_WA():
            """
            XXX: new test case failed!
                * TLE: 85 / 87 test cases passed.  [10000, 10000]*10000, k = 1000
                * TLE: 4 / 87 test cases passed.   [[2,2],[2,2],[2,2],[2,2],[2,2],[2,2]], k = 6
            """
            l, r = 0, len(points) - 1
            while l < r:
                mid = lomuto(points, l, r)
                if mid >= k - 1:
                    r = mid  # BUG: here causes INF Loop for the  given cases.
                else:
                    l = mid + 1
            return points[: l + 1]

        def qselect_fxr(l, r):
            """
            Runtime: 1472 ms, faster than 16.43% of Python3 online submissions for K Closest Points to Origin.

            T: O(N)
            """

            pi = lomuto(points, l, r)
            if pi == k - 1:
                return points[:k]
            elif pi < k - 1:
                return qselect_fxr(pi + 1, r)
            else:
                return qselect_fxr(l, pi - 1)

        # return qselect_fxr(0, len(points) - 1)

        def maxheap():
            """
            Runtime: 692 ms, faster than 53.18% of Python3 online submissions for K Closest Points to Origin.

            T: O(Nlogk)
            """
            pq = []
            for co in points:
                heappush(pq, (-dist(co), co))
                if len(pq) > k:
                    heappop(pq)
            return [tu[1] for tu in pq]

        def qsort():
            """
            Runtime: 1053 ms, faster than 55.02% of Python3 online submissions for K Closest Points to Origin.
            T: O(nlogn)
            """
            points.sort(key=dist)
            return points[:k]

        def kdtree():
            """
            https://leetcode.com/problems/k-closest-points-to-origin/discuss/576025/python-3-lines-knn-search-using-kd-tree-for-large-number-of-queries
            Followup: what if given 10 million points and search 10k times?
            Even qselect O(N) will TLE
            So we can use KD-Tree!
            - Build the tree: O(NlogN)
            - Search, Insert, Delete: O(logN)
            """
            kd = spatial.KDTree(points)
            dist, idx = kd.query(x=[0, 0], k=k, p=2)
            return [points[i] for i in idx] if k > 1 else [points[idx]]


sl = Solution()
# print(sl.kClosest(points=[[1, 3], [-2, 2]], k=1))
# print(sl.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))
# print(sl.kClosest(points=[[0, 1], [1, 0]], k=2))
# print(sl.kClosest([[68, 97], [34, -84], [60, 100], [2, 31], [-27, -38], [-73, -74], [-55, -39], [62, 91], [62, 92], [-57, -67]], 5))
print(sl.kClosest([[2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [1, 1]], 1))
print(sl.kClosest([[2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [1, 1]], 6))
print(sl.kClosest([[2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2]], 1))
print(sl.kClosest([[2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2]], 6))
