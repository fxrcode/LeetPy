"""
✅ GOOD DFS/BFS reachability

https://leetcode.com/list?selectedList=99566jt7
Neetcode Blind Curated 75
"""


from collections import deque
from typing import List

DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def os_bfs():
            """
            Runtime: 332 ms, faster than 47.09% of Python3 online submissions for Pacific Atlantic Water Flow.

            T/M: O(M*N) becase each cell explore exactly once!
            """
            mn = (len(heights), len(heights[0]))
            atlan = set()
            pacif = set()
            for r in range(mn[0]):
                atlan.add((r, mn[1] - 1))
                pacif.add((r, 0))
            for c in range(mn[1]):
                atlan.add((mn[0] - 1, c))
                pacif.add((0, c))

            def bfs(q):
                reachable = set()
                while q:
                    r, c = q.popleft()
                    # XXX: becase reachable is empty initially, need to add root here. OW. I need to init reachable beforehand
                    reachable.add((r, c))
                    for dx, dy in DIR:
                        x, y = r + dx, c + dy
                        if (
                            0 <= x < mn[0]
                            and 0 <= y < mn[1]
                            and (x, y) not in reachable
                            and heights[x][y] >= heights[r][c]
                        ):
                            # reachable.add((x, y))
                            q.append((x, y))
                return reachable

            reachable_atlan = bfs(deque(atlan))
            reachable_pacif = bfs(deque(pacif))
            ans = reachable_atlan.intersection(reachable_pacif)
            print(ans)
            return ans

        def fxr_dfs():
            """
            os: Runtime: 276 ms, faster than 87.75% of Python3 online submissions for Pacific Atlantic Water Flow.
                XXX: simply keep update reachable_atlan/pacif, rather use set() for each dfs
            os's T/M: O(M*N) becase each cell explore exactly once!


            fxr: Runtime: 988 ms, faster than 12.77% of Python3 online submissions for Pacific Atlantic Water Flow.

            """
            mn = (len(heights), len(heights[0]))
            atlan = set()
            pacif = set()
            for r in range(mn[0]):
                atlan.add((r, mn[1] - 1))
                pacif.add((r, 0))
            for c in range(mn[1]):
                atlan.add((mn[0] - 1, c))
                pacif.add((0, c))

            def dfs(r, c, visited):
                # XXX: DAMN, forgot dfs again! Memorize UCB algorithm!
                visited.add((r, c))
                for dx, dy in DIR:
                    x, y = r + dx, c + dy
                    if (
                        0 <= x < mn[0]
                        and 0 <= y < mn[1]
                        and (x, y) not in visited
                        and heights[x][y] >= heights[r][c]
                    ):
                        dfs(x, y, visited)

            reachable_atlan = set()
            reachable_pacif = set()
            for r, c in atlan:
                # visited = set()
                # dfs(r, c, visited)
                # reachable_atlan.update(visited)
                dfs(r, c, reachable_atlan)
            for r, c in pacif:
                # visited = set()
                # dfs(r, c, visited)
                # reachable_pacif.update(visited)
                dfs(r, c, reachable_pacif)

            ans = reachable_atlan.intersection(reachable_pacif)
            print(ans)
            return ans

        def fxr_bt_TLE():
            """
            TLE: 112 / 113 test cases passed. This case is all bottom line = 0!
            """
            mn = (len(heights), len(heights[0]))
            atlan = set()
            pacif = set()
            for r in range(mn[0]):
                atlan.add((r, mn[1] - 1))
                pacif.add((r, 0))
            for c in range(mn[1]):
                atlan.add((mn[0] - 1, c))
                pacif.add((0, c))

            def bt(r, c, visited, ocean):
                if (r, c) in ocean:
                    return True
                ans = False
                for dx, dy in DIR:
                    x, y = r + dx, c + dy
                    if (
                        0 <= x < mn[0]
                        and 0 <= y < mn[1]
                        and (x, y) not in visited
                        and heights[x][y] <= heights[r][c]
                    ):
                        visited.add((x, y))
                        if bt(x, y, visited, ocean):
                            ans = True
                            break
                        visited.remove((x, y))
                return ans

            res = []
            for r in range(mn[0]):
                for c in range(mn[1]):
                    if bt(r, c, set(), atlan) and bt(r, c, set(), pacif):
                        res.append([r, c])
            print(res)
            return res

        def fxr_dp_WA():
            """
            WA: 50 / 113 test cases passed.

            case: [[1,2,3],[8,9,4],[7,6,5]]
            """
            m, n = len(heights), len(heights[0])

            atlan_true = set()
            pacif_true = set()
            # atlan
            atlan = [[False] * n for _ in range(m)]
            for c in range(n):
                atlan[-1][c] = True
                atlan_true.add((m - 1, c))
            for r in range(m):
                atlan[r][-1] = True
                atlan_true.add((r, n - 1))
            for r in reversed(range(m - 1)):
                for c in reversed(range(n - 1)):
                    for rr, cc in [(r, c + 1), (r + 1, c)]:
                        atlan[r][c] |= (heights[r][c] >= heights[rr][cc]) and atlan[rr][
                            cc
                        ]
                    if atlan[r][c]:
                        atlan_true.add((r, c))

            # pacific
            pacif = [[False] * n for _ in range(m)]
            for c in range(n):
                pacif[0][c] = True
                pacif_true.add((0, c))
            for r in range(m):
                pacif[r][0] = True
                pacif_true.add((r, 0))

            for r in range(1, m):
                for c in range(1, n):
                    for rr, cc in [(r, c - 1), (r - 1, c)]:
                        pacif[r][c] |= (heights[r][c] >= heights[rr][cc]) and pacif[rr][
                            cc
                        ]
                    if pacif[r][c]:
                        pacif_true.add((r, c))

            print(atlan_true)
            print(pacif_true)
            ans = [[r, c] for r, c in pacif_true.intersection(atlan_true)]
            print(ans)
            return ans

        # return fxr_dp_WA()
        # return fxr_dfs()
        return os_bfs()


sl = Solution()
# sl.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1],
#                     [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
sl.pacificAtlantic([[1, 2, 3], [8, 9, 4], [7, 6, 5]])
