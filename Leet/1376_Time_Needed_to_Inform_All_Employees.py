"""
tag: medium, DFS
Lookback:
- Study plan: coding skills I
- My instinct: Dijkstra for longest path
- similar: 743. Network Delay Time
"""
from collections import defaultdict
from functools import cache
from heapq import heappop, heappush
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def fxr():
            """
            Runtime: 1192 ms, faster than 99.23% of Python3 online submissions for Time Needed to Inform All Employees.

            bottom-up DFS
            """

            @cache
            def dfs(e):
                m = manager[e]
                if m == -1:
                    return 0
                return informTime[m] + dfs(m)

            return max(map(dfs, range(n)))

        def dijkstra_localhostghost():
            """
            https://leetcode.com/problems/time-needed-to-inform-all-employees/discuss/532530/Python3-Easy-Python-Solution%3A-DijkstraBFSDFS
            # 743. Network Delay Time
            """
            AL = defaultdict(list)
            for i, m in enumerate(manager):
                AL[m].append((informTime[i], i))
            dist = {}
            pq = [(informTime[headID], headID)]

            while pq:
                time, u = heappop(pq)
                # similar to Dijkstra but not Dijkstra, cuz each Root->node path is unique in Tree, rather as in Graph. So dist[u] is const so set once.
                if u in dist:
                    continue
                for w, v in AL[u]:
                    if v in dist:
                        continue
                    heappush(pq, (time + w, v))
            return max(dist.values())

        def lee215_topdown():
            AL = [[] for i in range(n)]
            for s, m in enumerate(manager):
                AL[m].append(s)

            def dfs(i):
                return max([dfs(j) for j in AL[i]] or [0]) + informTime[i]

            return dfs(headID)

        return fxr()


sl = Solution()
print(sl.numOfMinutes(n=6, headID=2, manager=[2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0]))
assert sl.numOfMinutes(n=1, headID=0, manager=[-1], informTime=[0]) == 0
assert sl.numOfMinutes(n=11, headID=4, manager=[5, 9, 6, 10, -1, 8, 9, 1, 9, 3, 4], informTime=[0, 213, 0, 253, 686, 170, 975, 0, 261, 309, 337]) == 2560
