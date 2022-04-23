"""
tag: medium, topo-sort
Lookback:
- 9chap BFS topo-sort template, can check if topo-sort exist or not (aka cycle detect), unique topo-sort
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def ch9_bfs():
            """
            Runtime: 188 ms, faster than 21.17% of Python3 online submissions for Course Schedule.

            """
            AL = defaultdict(list)
            #! must use Dictionary Comprehension, rather defaultdict
            DEG = {v: 0 for v in range(numCourses)}
            for a, b in prerequisites:
                AL[b].append(a)
                DEG[a] += 1

            q = deque([v for v in DEG if DEG[v] == 0])
            ts = []
            while q:
                u = q.popleft()
                ts.append(u)
                if len(ts) == numCourses:
                    return True
                for v in AL[u]:
                    DEG[v] -= 1
                    if DEG[v] == 0:
                        q.append(v)
            return False

        return ch9_bfs()

        def os_210():
            """
            Runtime: 199 ms, faster than 8.48% of Python3 online submissions for Course Schedule.

            XXX: modified from 210 os: https://leetcode.com/problems/course-schedule-ii/solution/
            T: O(V+E)
            """
            WHITE, GRAY, BLACK = 0, 1, 2

            def check_deadlock(u) -> bool:
                nonlocal dfn, cyclic
                if cyclic:
                    return
                dfn[u] = GRAY
                for v in AL[u]:
                    if dfn[v] == WHITE:
                        check_deadlock(v)
                    elif dfn[v] == GRAY:
                        cyclic = True
                dfn[u] = BLACK

            AL = {i: [] for i in range(numCourses)}
            for a, b in prerequisites:
                AL[b].append(a)
            dfn = [WHITE] * numCourses
            cyclic = False

            for i in range(numCourses):
                if not cyclic:
                    check_deadlock(i)
            return cyclic == False


sl = Solution()
# numCourses = 2
# prerequisites = [[0, 1]]
# numCourses = 5
# prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]

print(sl.canFinish(numCourses=2, prerequisites=[[1, 0]]))
print(sl.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))
