"""
https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3910/
Leetcode Explore Graph: Disjoint Set

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Insight
There are so many different approaches and so many different ways to implement each. I find it hard to decide, so here are several :-)
In all of them, I check one of these tree characterizations:
* Has n-1 edges and is acyclic.
* Has n-1 edges and is connected.

"""


from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def fxr_1():
            """
            Runtime: 96 ms, faster than 57.84% of Python3 online submissions for Graph Valid Tree.

            AC in 2nd. 1st got WA for multiple trees!
            """
            uf = {i: i for i in range(n)}

            def find(x):
                if x != uf[x]:
                    uf[x] = find(uf[x])
                return uf[x]

            for i, j in edges:
                ri, rj = find(i), find(j)
                if ri == rj:
                    return False
                uf[find(j)] = find(i)
            # return sum(i == f for i, f in uf.items()) == 1
            return len(edges) == n - 1

        return fxr_1()


sl = Solution()
print(sl.validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]]))
print(sl.validTree(n=5, edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
print(sl.validTree(n=4, edges=[[0, 1], [2, 3]]))
