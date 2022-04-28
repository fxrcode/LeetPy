"""
✅ GOOD Dijkstra augment
Tag: Medium, Graph
Lookback:

TODO: BFS+Binary Search, Union-Find.
https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3952/
Leetcode Explore Graph: SSSP

"""


from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        INF = 1e7

        def dijkstra_hiepit():
            """
            Your runtime beats 58.75 % of python3 submissions.
            REF: https://leetcode.com/problems/path-with-minimum-effort/discuss/909017/JavaPython-Dijikstra-Binary-search-Clean-and-Concise
            https://leetcode.com/problems/path-with-minimum-effort/discuss/913076/python-Using-union-find-(Anyone-else-use-this-approach)
            https://leetcode.com/problems/path-with-minimum-effort/discuss/909002/JavaPython-3-3-codes%3A-Binary-Search-Bellman-Ford-and-Dijkstra-w-brief-explanation-and-analysis.

            XXX: blackbean123: my understanding of why we can use Dijkstra here:
            1. here, the total path cost is the maximum absolute difference, its a different kind of cost function
                compared to the vanilla adding all costs together along the path
            2. for Dijkstra, edge weight cannot be negative, but what does that really mean. It effectively means
                total path cost cannot go down when a new edge joins the path. In the vanilla Dijkstra, it's in the
                form of negative edge weight. If we translate that to this problem, we can see that the total path
                cost (maximum absolute difference) will never go down when a new edge joins the path

            E=V=m*n
            T: O(ElogV), M: O(V)
            """
            m, n = len(heights), len(heights[0])
            dist = [[INF] * n for _ in range(m)]
            src, dst = (0, 0), (m - 1, n - 1)
            pq = [(0, src)]  # dist, row/col
            while pq:
                d, (r, c) = heappop(pq)
                if d > dist[r][c]:
                    continue
                if (r, c) == dst:
                    return d
                for i in range(4):
                    xx, yy = r + DIR[i][0], c + DIR[i][1]
                    if not (0 <= xx < m and 0 <= yy < n):
                        continue
                    new_dist = max(d, abs(heights[xx][yy] - heights[r][c]))
                    if dist[xx][yy] > new_dist:
                        dist[xx][yy] = new_dist
                        heappush(pq, (new_dist, (xx, yy)))

        """
        BUG: misunderstood the condition: minimize the maxximum absolute difference
        def dijkstra_fxr():
            def eff(c0, c1):
                x0, y0 = c0
                x1, y1 = c1
                return abs(heights[x0][y0] - heights[x1][y1])

            def route(pre, src, dst):
                cur = dst
                r = []
                while cur != src:
                    r.append(cur)
                    cur = pre[cur]
                return [src]+r[::-1]

            R, C = len(heights), len(heights[0])
            src, dst = (0, 0), (R-1, C-1)
            dist = {}
            dist[src] = 0
            pre = {}
            pq = [(0, src)]
            while pq:
                d, (x, y) = heappop(pq)
                if d > dist.setdefault((x, y), INF):
                    continue
                for dx, dy in DIR:
                    xx, yy = x+dx, y+dy
                    if not (0 <= xx < R and 0 <= yy < C):
                        continue
                    dU, dV, wUV = dist[(x, y)], \
                        dist.setdefault((xx, yy), INF), eff((x, y), (xx, yy))
                    if dU + wUV >= dV:
                        continue
                    pre[(xx, yy)] = (x, y)
                    dist[(xx, yy)] = dU+wUV
                    heappush(pq, (dist[(xx, yy)], (xx, yy)))
            print(route(pre, src, dst))

            print(dist)
            return dist[dst]
        """

        return dijkstra_hiepit()


sl = Solution()
print(sl.minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
