"""
✅ GOOD MST (PQ + UF)
Tag: Medium, MST, Graph, UF, Greedy
Lookback:
- Kruskal
- Prim
https://leetcode.com/explore/learn/card/graph/621/algorithms-to-construct-minimum-spanning-tree/3857/
Leetcode Explore Graph: MST

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

"""


from heapq import heappop, heappush
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def prim_idontknoooo() -> int:
            """
            Runtime: 1816 ms, faster than 71.89% of Python3 online submissions for Min Cost to Connect All Points.
            REF: https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/843995/Python-3-or-Min-Spanning-Tree-or-Prim's-Algorithm
                * an optimized/elegant version by darkTianTian in reply: no need to init pq with ALL O(N^2) edges, can do it on fly

            Prim: O(NlogN)
            """

            def manhattan(p1, p2):
                return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

            mst, n = 0, len(points)
            vis = set()
            #! (0,0) is not point coordinate but rather the src and target vertices
            vertices = [(0, (0, 0))]
            while len(vis) < n:
                # XXX: how to think clearly?
                # Ans:
                #   1. coding according to visual example.
                #   2. be clear on what states need to updated, don't miss any states (aka vars)
                #   3. naming wisely! eg. use vertices to represent the priority queue, rather pq!
                d, (u, v) = heappop(vertices)

                # XXX: why check seen? A: because pq only pop shortest one but also contains all candidates.
                if v in vis:
                    continue
                mst += d
                vis.add(v)
                for j in range(n):
                    if j not in vis and j != v:
                        heappush(vertices, (manhattan(points[v], points[j]), (v, j)))
            return mst

        return prim_idontknoooo()

        def kruskal_hiepit() -> int:
            """
            Your runtime beats 81.16 % of python3 submissions.
            https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/1476951/Python-2-solutions%3A-Kruskal-and-Prim-Standard-code-Clean-and-Concise
            T: O(ElogV)
            """

            def manhattan(i, j):
                x0, y0 = points[i]
                x1, y1 = points[j]
                return abs(x0 - x1) + abs(y0 - y1)

            def find(i):
                if uf[i] != i:
                    uf[i] = find(uf[i])
                return uf[i]

            def union(i, j):
                x, y = find(i), find(j)
                if x == y:
                    return False
                if sz[x] > sz[y]:
                    x, y = y, x
                # make sure group(x) <= group(y), so merge small into big
                uf[x] = y
                sz[y] += sz[x]
                nonlocal groups
                groups -= 1
                return True

            pq = []
            groups = n = len(points)
            uf = {i: i for i in range(n)}
            sz = [1] * n
            for i in range(n):
                for j in range(i + 1, n):
                    heappush(pq, (manhattan(i, j), (i, j)))

            mst = 0
            while pq and groups > 1:
                d, (i, j) = heappop(pq)
                if union(i, j):
                    mst += d
            return mst

        return kruskal_hiepit()


sl = Solution()
print(sl.minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
print(sl.minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]))
print(sl.minCostConnectPoints(points=[[0, 0]]))
