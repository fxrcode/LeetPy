'''
https://leetcode.com/explore/learn/card/graph/623/kahns-algorithm-for-topological-sorting/3953/
Leetcode Explore Graph: Topological Sort

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
'''


from typing import List
from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def toposort():
            """
            Runtime: 256 ms, faster than 38.41% of Python3 online submissions for Minimum Height Trees.

            XXX: TopoSort BFS: O(V+E)
            """
            if n <= 2:
                # for edge cases
                return [i for i in range(n)]

            AL = defaultdict(set)
            # counter = defaultdict(int)
            for u, v in edges:
                AL[u].add(v)
                AL[v].add(u)
                # counter[u] += 1
                # counter[v] += 1

            leaves = deque([n for n in AL if len(AL[n]) == 1])

            remaining_nodes = n
            while leaves and remaining_nodes > 2:
                qlen = len(leaves)
                for _ in range(qlen):
                    leaf = leaves.popleft()
                    # remove leaf/neig (both edge)
                    # XXX: leaf node has only SINGLE neigbhor
                    neig = AL[leaf].pop()
                    AL[neig].remove(leaf)
                    if len(AL[neig]) == 1:
                        leaves.append(neig)
                    remaining_nodes -= 1

            return list(leaves)

        return toposort()


sl = Solution()
print(sl.findMinHeightTrees(n=1, edges=[]))
print(sl.findMinHeightTrees(n=6,
                            edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
print(sl.findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]))
