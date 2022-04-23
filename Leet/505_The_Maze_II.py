'''
Chris Mock (Dec 12, 2021)
'''

import heapq
from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        def cenkay():
            """
            Runtime: 288 ms, faster than 92.37% of Python3 online submissions for The Maze II.

            XXX: elegant code and return asap hit destination
            T: O(ElogV), here E=V=m*n
            """
            m, n, q = len(maze), len(maze[0]), [(0, start[0], start[1])]
            dist = defaultdict(lambda: 1e6)
            dist[(start[0], start[1])] = 0
            while q:
                d, x, y = heapq.heappop(q)
                if d > dist[(x, y)]:
                    continue
                if [x, y] == destination:
                    return d
                for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    xx, yy, w = x, y, 0
                    while 0 <= xx + i < m and 0 <= yy + j < n and maze[xx + i][yy + j] == 0:
                        xx += i
                        yy += j
                        w += 1
                    if d + w < dist[(xx, yy)]:
                        dist[(xx, yy)] = d + w
                        heapq.heappush(q, (d + w, xx, yy))
            return -1

        def fxr_dijk():
            """
            Runtime: 312 ms, faster than 70.54% of Python3 online submissions for The Maze II.

            XXX: 1st time recite Dijkstra (CP4 lazy variant)
            """
            def neighs(x, y):
                vs = []
                m, n = len(maze), len(maze[0])
                # left,right bound
                yy = y
                while yy < n and maze[x][yy] == 0:
                    yy += 1
                vs.append((x, yy-1))
                yy = y
                while yy >= 0 and maze[x][yy] == 0:
                    yy -= 1
                vs.append((x, yy+1))

                # top,bottom bound
                xx = x
                while xx >= 0 and maze[xx][y] == 0:
                    xx -= 1
                vs.append((xx+1, y))
                xx = x
                while xx < m and maze[xx][y] == 0:
                    xx += 1
                vs.append((xx-1, y))
                return vs

            def duv(u, v):
                return abs(u[0]-v[0]) + abs(u[1]-v[1])

            dist = defaultdict(lambda: 1e9)
            src = (start[0], start[1])
            dst = (destination[0], destination[1])
            dist[src] = 0
            pq = [(0, src)]
            while pq:
                d, u = heappop(pq)
                if d > dist[u]:
                    continue
                for v in neighs(*u):
                    w = duv(u, v)
                    if dist[v] <= dist[u] + w:
                        continue
                    dist[v] = dist[u] + w
                    heappush(pq, (dist[v], v))

            if dist[dst] == 1e9:
                return -1
            return dist[dst]

        return fxr_dijk()


sl = Solution()
print(sl.shortestDistance(maze=[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [
      1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], start=[0, 4], destination=[4, 4]))
print(sl.shortestDistance(maze=[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [
      1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], start=[0, 4], destination=[3, 2]))
