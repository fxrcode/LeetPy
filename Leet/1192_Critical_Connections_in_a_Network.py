"""
📌✅ GOOD DFS (Tarjan algs)
Tag: Hard, DFS, Graph
Lookback:
- How to invent Tarjan by yourself in 45min interview?
"""

from collections import defaultdict
from typing import List


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        def os_tarjan_cp4():
            """
            Runtime: 2580 ms, faster than 73.49% of Python3 online submissions for Critical Connections in a Network.

            https://leetcode.com/problems/critical-connections-in-a-network/discuss/382526/Tarjan-Algorithm-(DFS)-Python-Solution-with-explanation/487257
            T: O(V+E)
            """
            self.num = 0
            dfn = [None] * n
            low = [None] * n
            AL = defaultdict(list)
            for u, v in connections:
                AL[u].append(v)
                AL[v].append(u)
            res = []

            def dfs(u, par):
                if dfn[u] is not None:
                    return
                dfn[u] = low[u] = self.num
                self.num += 1
                for v in AL[u]:
                    if dfn[v] is None:
                        dfs(v, u)
                # minimal num in the neighbors except direct parent
                low[u] = min([dfn[u]] + [low[v] for v in AL[u] if v != par])

            dfs(0, None)
            for u, v in connections:
                # non bridge
                if low[u] > dfn[v] or low[v] > dfn[u]:
                    res.append([u, v])
            return res

        return os_tarjan_cp4()


sl = Solution()
print(sl.criticalConnections(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]]))
print(sl.criticalConnections(n=2, connections=[[0, 1]]))
