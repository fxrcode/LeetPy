"""
https://leetcode.com/explore/learn/card/graph/621/algorithms-to-construct-minimum-spanning-tree/3857/
Leetcode Explore Graph: MST

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

TODO: Prim algs
"""


from heapq import heappop, heappush
from typing import List


class Solution:
    def minCostConnectPoints_prim(self, points: List[List[int]]) -> int:
        """
        Your runtime beats 42.36 % of python3 submissions.

        REF: https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/843995/Python-3-or-Min-Spanning-Tree-or-Prim's-Algorithm
            * an optimized/elegant version by darkTianTian in reply: no need to init pq with ALL O(N^2) edges, can do it on the fly

        Prim: O(NlogN)
        """

        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        ans, n = 0, len(points)
        seen = set()
        # XXX: just notice this is same as Dijkstra to init pq with [(0,s)]
        # weight, p_idx_0 -> p_idx_0 to init the pq! So elegant!
        vertices = [0, (0, 0)]
        while len(seen) < n:
            # XXX: how to think clearly?
            # Ans:
            #   1. coding according to visual example.
            #   2. be clear on what states need to updated, don't miss any states (aka vars)
            #   3. naming wisely! eg. use vertices to repesent the priority queue, rather pq!
            w, (u, v) = heappop(vertices)

            # XXX: why need to check seen? A: because pq only pop shortest one but also contains all candidates.
            if v in seen:
                continue
            ans += w
            seen.add(v)
            for j in range(n):
                if j not in seen and j != v:
                    heappush(vertices, (manhattan(points[v], points[j]), (v, j)))
        return ans

    def minCostConnectPoints_kruskal_hobiter(self, points: List[List[int]]) -> int:
        """
        Your runtime beats 81.16 % of python3 submissions.

        REF: https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/844107/Java-Minimum-Spanning-Tree-and-Union-Find-with-Optimization-Beat-100
        translate from hobiter's java impl to Python

        XXX: stick to simplist UF, with 0~n-1 index to node bi-direction mapping. only use coord for manhattan calculation

        T: O(ElogE)
        """

        def manhatan(i, j):
            x0, y0 = points[i]
            x1, y1 = points[j]
            return abs(x0 - x1) + abs(y0 - y1)

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False

            # not same group, so union them
            if rank[rx] < rank[ry]:
                uf[rx] = ry
            else:
                uf[ry] = rx
                if rank[rx] == rank[ry]:
                    # BUG: uf[ry] = rx. The same rank check is just for rank += 1!
                    rank[rx] += 1

            nonlocal groups
            groups -= 1
            return True

        pq = []
        groups = n = len(points)
        uf = {i: i for i in range(n)}
        rank = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                heappush(pq, (manhatan(i, j), (i, j)))

        mst = 0
        while pq and groups > 1:
            d, (i, j) = heappop(pq)
            if union(i, j):
                mst += d
        return mst

    def minCostConnectPoints_kruskal_fxr(self, points: List[List[int]]) -> int:
        """
        Your runtime beats 44.37 % of python3 submissions.

        XXX: spent 50min on this problem, confused by uf's on point, where we got coord here.
        """
        uf = {}
        pq = []
        groups = len(points)

        def manhatan(idx1, idx2) -> int:
            x1, y1 = points[idx1]
            x2, y2 = points[idx2]
            return abs(x1 - x2) + abs(y1 - y2)

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False

            # if not same root, union these 2 points
            uf[ry] = rx

            # XXX: have to use nonlocal or global to access outer scope
            # Most python objects (booleans, integers, floats, strings, and tuples) are immutable.
            nonlocal groups
            groups -= 1
            return True

        def kruskal():
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    heappush(pq, (manhatan(i, j), (i, j)))

            # init uf
            for x, y in points:
                uf[(x, y)] = (x, y)

            mst = []
            while pq and groups > 1:
                min_manha, (i, j) = heappop(pq)
                x1, y1 = points[i]
                x2, y2 = points[j]
                if union((x1, y1), (x2, y2)):
                    mst.append(min_manha)
            return sum(mst)

        return kruskal()


sl = Solution()
print(sl.minCostConnectPoints_kruskal_hobiter(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))

print(sl.minCostConnectPoints_kruskal_hobiter(points=[[3, 12], [-2, 5], [-4, 1]]))
print(sl.minCostConnectPoints_kruskal_hobiter(points=[[0, 0]]))
