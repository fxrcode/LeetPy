'''
York Mork (Dec 28)

Tag: Medium, TopoSort
Lookback:
- topo-sort DFS is handy, not only return ts[], but also return bool to see if it leads to a valid ts
'''

from collections import defaultdict
from typing import List


class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        def os_topo():
            """
            Runtime: 692 ms, faster than 80.52% of Python3 online submissions for Find Eventual Safe States.

            T: O(E+V)
            """
            W, G, B = 0, 1, 2
            colr = defaultdict(int)

            def dfs(u):
                if colr[u] != W:
                    return colr[u] == B

                colr[u] = G
                for v in graph[u]:
                    if colr[v] == B:
                        continue
                    if colr[v] == G or not dfs(v):
                        return False
                colr[u] = B
                return True

            return list(filter(dfs, range(len(graph))))

        return os_topo()


sl = Solution()
print(sl.eventualSafeNodes(graph=[[1, 2], [2, 3], [5], [0], [5], [], []]))
