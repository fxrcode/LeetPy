"""
✅ GOOD Dijkstra augment
Tag: Medium, Graph, Dijkstra, BFS/DFS, Bisect
Lookback:
- Dijkstra Variation
- Binary search + BFS/DFS
Similar:
- (Coinbase) 1514. Path with Maximum Probability https://leetcode.com/problems/path-with-maximum-probability/discuss/731767/JavaPython-3-2-codes%3A-Bellman-Ford-and-Dijkstra's-algorithm-w-brief-explanation-and-analysis
- 778. Swim in Rising Water
- 1631. Path With Minimum Effort
- 1514. Path with Maximum Probability
- 1102. Path With Maximum Minimum Value 
https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3952/
Leetcode Explore Graph: SSSP
"""
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        INF = 2e9

        def dbabichev_bisect_dfs():
            """
            Runtime: 5816 ms, faster than 5.47% of Python3 online submissions for Path With Minimum Effort.
            T: O(MNlog(max(height)))
            """
            m, n = len(heights), len(heights[0])

            def dfs(LIMIT, i, j):
                vis.add((i, j))
                for dx, dy in DIR:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and (x, y) not in vis:
                        if abs(heights[i][j] - heights[x][y]) <= LIMIT:
                            dfs(LIMIT, x, y)

            l, r = 0, max(max(heights, key=max))
            while l < r:
                mid = (l + r) // 2
                vis = set()
                dfs(mid, 0, 0)
                if (m - 1, n - 1) in vis:
                    r = mid
                else:
                    l = mid + 1
            return l

        return dbabichev_bisect_dfs()

        def dijkstra_hiepit():
            """
            Runtime: 823 ms, faster than 83.58% of Python3 online submissions for Path With Minimum Effort.

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
                for dx, dy in DIR:
                    xx, yy = r + dx, c + dy
                    if not (0 <= xx < m and 0 <= yy < n):
                        continue
                    new_dist = max(d, abs(heights[xx][yy] - heights[r][c]))
                    if dist[xx][yy] > new_dist:
                        dist[xx][yy] = new_dist
                        heappush(pq, (new_dist, (xx, yy)))

        return dijkstra_hiepit()
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


sl = Solution()
print(sl.minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
print(sl.minimumEffortPath(heights=[[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
print(
    sl.minimumEffortPath(
        heights=[
            [1, 2, 1, 1, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 1, 1, 2, 1],
        ]
    )
)
