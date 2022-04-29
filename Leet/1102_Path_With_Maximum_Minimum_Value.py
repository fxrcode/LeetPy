"""
✅ GOOD BFS (Dijkstra)
✅ GOOD Greedy (Dijkstra)
✅ GOOD UF (Swim in Rising Water)
✅ GOOD Bisect
tag: Medium, BFS, DFS, heapq, bisect, UF
Lookback:
- Minimax as greedy option in Dijkstra
- 1st time seen UF usage in this way :-)
Similar:
- 778. Swim in Rising Water
- 1631. Path With Minimum Effort
- 1514. Path with Maximum Probability
"""
from heapq import heappop, heappush
from typing import List


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        def os_uf():
            """
            Runtime: 1968 ms, faster than 53.81% of Python3 online submissions for Path With Maximum Minimum Value.

            XXX: like GAME!
            """
            R, C = len(grid), len(grid[0])
            root = list(range(R * C))
            sz = [1] * (R * C)
            D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            visited = set()

            def find(i):
                if i != root[i]:
                    root[i] = find(root[i])
                return root[i]

            def union(i, j):
                x, y = map(find, [i, j])
                if x == y:
                    return
                if sz[x] > sz[y]:
                    x, y = y, x
                # make sure px is smaller coorp
                root[x] = y
                sz[y] += sz[x]

            vals = [(r, c) for r in range(R) for c in range(C)]
            vals.sort(key=lambda x: grid[x[0]][x[1]], reverse=True)
            for i, j in vals:
                visited.add((i, j))
                for di, dj in D:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < R and 0 <= jj < C and (ii, jj) in visited:
                        # XXX: only union if cur and neighbor are visited
                        p, pp = i * C + j, ii * C + jj
                        union(p, pp)
                        # check if top-left is connected w/ bottom-right
                        if find(0) == find(R * C - 1):
                            return grid[i][j]
            return -1

        return os_uf()

        def deigo_bfs_pq():
            """
            Runtime: 1384 ms, faster than 85.36% of Python3 online submissions for Path With Maximum Minimum Value.

            REF: https://leetcode.com/problems/path-with-maximum-minimum-value/discuss/416227/Python-Dijkstra-Binary-Search-%2B-DFS-Union-Find-complexity-analysis
            """

            def mxpq_push(v, x, y):
                heappush(mxpq, (-v, x, y))

            def mxpq_pop():
                negv, x, y = heappop(mxpq)
                return -negv, x, y

            mxpq = []
            mxpq_push(grid[0][0], 0, 0)
            seen = set([(0, 0)])
            D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            m, n = len(grid), len(grid[0])
            while mxpq:
                score, x, y = mxpq_pop()
                if (x, y) == (m - 1, n - 1):
                    return score
                for dx, dy in D:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in seen:
                        # Crux, greedy to stay in max(min) path.
                        # b/c we need to greedy choose max, so use maxheap, then push (-score)
                        # score = min(path), since we use neg due to maxheap, min(path) === max(-path)
                        mxpq_push(min(score, grid[xx][yy]), xx, yy)
                        seen.add((xx, yy))
            return -1

        return deigo_bfs_pq()


sl = Solution()
assert (
    sl.maximumMinimumPath(
        grid=[[3, 4, 6, 3, 4], [0, 2, 1, 1, 7], [8, 8, 3, 2, 7], [3, 2, 4, 9, 8], [4, 1, 2, 0, 0], [4, 6, 5, 4, 3]]
    )
    == 3
)
