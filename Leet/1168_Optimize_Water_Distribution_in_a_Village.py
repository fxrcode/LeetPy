"""
✅ GOOD UF (MST)
tag: medium, UF, Graph
https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3916/
Leetcode Explore Graph: Disjoint Set Union (DSU)


There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.
For each house i, we can either build a well inside it directly with cost wells[i - 1] (note the -1 due to 0-indexing), or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes, where each pipes[j] = [house1j, house2j, costj] represents the cost to connect house1j and house2j together using a pipe. Connections are bidirectional.
Return the minimum total cost to supply water to all houses.

XXX: there's only 1 MST implement in practice: Kruskal's UF (quote in CP4)
"""

from typing import List


class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: List[int], pipes: List[List[int]]
    ) -> int:
        """
        REF: official solution and lee215
        Runtime: 525 ms, faster than 56.99% of Python3 online submissions for Optimize Water Distribution in a Village.

        ✅ How to re-state problem still differently (say, reduce to common topics).
            How to be creative as top coders? Learn thoughts/tips from them.
        """
        # don't forget the well is virtual node: 0
        uf = {i: i for i in range(n + 1)}

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        # XXX: first time seeing start used in practice
        w = [(c, i, 0) for i, c in enumerate(wells, start=1)]
        p = [(c, x, y) for x, y, c in pipes]
        groups = n + 1
        mst = 0
        for c, x, y in sorted(w + p, key=lambda x: x[0]):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                continue
            uf[root_y] = root_x
            mst += c
            groups -= 1
            if groups == 1:
                return mst

        # print(groups, mst)
        return -1


sl = Solution()
print(sl.minCostToSupplyWater(n=3, wells=[1, 2, 2], pipes=[[1, 2, 1], [2, 3, 1]]))
