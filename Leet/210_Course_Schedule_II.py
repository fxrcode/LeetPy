"""
✅ GOOD Graph (Topological Sort)
Daily Challenge (Dec 23)

https://leetcode.com/explore/learn/card/graph/623/kahns-algorithm-for-topological-sorting/3868/
Leetcode Explore Graph: Topological Sort

* BFS & DFS topological sort

tag: topo-sort, dfs, bfs
Lookback:
- 9chap recommends BFS, which make sense and never SOF.
- both BFS/DFS topo-sort can detect cycle.
- 9chap: BFS can find if topo-sort unique
"""


from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def kahn_fxr():
            """
            Runtime: 139 ms, faster than 57.89% of Python3 online submissions for Course Schedule II.

            T: O(E+V)
            """
            AL = defaultdict(list)
            DEG = {u: 0 for u in range(numCourses)}
            for c, p in prerequisites:
                AL[p].append(c)
                DEG[c] += 1
            m = numCourses
            q = deque([i for i in range(m) if DEG[i] == 0])
            ts = []
            while q:
                u = q.popleft()
                ts.append(u)
                if len(ts) == m:
                    return ts
                for v in AL[u]:
                    DEG[v] -= 1
                    if DEG[v] == 0:
                        q.append(v)
            return []

        return kahn_fxr()

        def os_dfs():
            """
            Runtime: 104 ms, faster than 43.92% of Python3 online submissions for Course Schedule II.

            XXX: no need of visited set, since CLRS depends on dfn (aka color)
            """
            WHITE, GRAY, BLACK = 0, 1, 2
            possible = True
            ts = []
            color = defaultdict(int)

            AL = defaultdict(list)
            for c, p in prerequisites:
                AL[p].append(c)

            def dfs(u):
                nonlocal possible
                if not possible:
                    return
                color[u] = GRAY
                for v in AL[u]:
                    if color[v] == WHITE:
                        dfs(v)
                    elif color[v] == GRAY:
                        possible = False
                color[u] = BLACK
                ts.append(u)

            for u in range(numCourses):
                if color[u] == WHITE:
                    dfs(u)
            return ts[::-1] if possible else []

        # return os_dfs()


sl = Solution()
print(sl.findOrder(numCourses=2, prerequisites=[[1, 0]]))
print(sl.findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))
print(sl.findOrder(numCourses=1, prerequisites=[]))
print(sl.findOrder(3, [[1, 0], [1, 2], [0, 1]]))
