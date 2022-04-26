"""
✅ GOOD BFS (bi-directional)
✅ GOOD DP (memo-DFS)
Tag: Medium, BFS, logic, DFS
Lookback:
- Insight: prune logic based on symmetry, meaning (x, y), (-x, y), (x, -y), (-x, -y) will have the same results.
"""


from collections import deque
from functools import cache


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        def idontknoooo_dp():
            """
            Runtime: 88 ms, faster than 84.58% of Python3 online submissions for Minimum Knight Moves.

            Top-down DP => memo DFS => backward thinking.
            Goal: origin -> target
            Backward: target -> origin
            - Backward thinking in ALL recursion (Balloon, TSP DP), as well in #991
            """

            @cache
            def dp(x, y):
                if x + y == 0:
                    return 0
                elif x + y == 2:
                    return 2
                return min(dp(abs(x - 1), abs(y - 2)), dp(abs(x - 2), abs(y - 1))) + 1

            return dp(abs(x), abs(y))

        def idontknoooo_bfs():
            """
            basic BFS w/ logic: symmetric & prune
            """
            nonlocal x, y
            # no need to have (-1, -2) and (-2, -1) since it only goes 1 direction
            DIR = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1)]
            q = deque([(0, 0)])
            step = 0
            x, y, vis = abs(x), abs(y), set([(0, 0)])
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    if (i, j) == (x, y):
                        return step
                    for dx, dy in DIR:
                        ii, jj = i + dx, j + dy
                        if (ii, jj) not in vis and -1 <= ii <= x + 2 and -1 <= jj <= y + 2:
                            vis.add((ii, jj))
                            q.append((ii, jj))
                step += 1
            return -1

        # return idontknoooo_bfs()

        def fxr_bibfs():
            """
            Runtime: 621 ms, faster than 72.89% of Python3 online submissions for Minimum Knight Moves.
            https://leetcode.com/problems/minimum-knight-moves/discuss/947138/Python-3-or-BFS-DFS-Math-or-Explanation
            """
            nonlocal x, y
            x, y = abs(x), abs(y)
            q1, q2 = set([(0, 0)]), set([(x, y)])
            step = 0
            vis = set([(0, 0), (x, y)])
            DIR = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
            while q1:
                if len(q1) > len(q2):
                    q1, q2 = q2, q1
                q1_nxt = set()
                for i, j in q1:
                    # option1:  q1 as candidate
                    if (i, j) in q2:
                        return step
                    for dx, dy in DIR:
                        ii, jj = i + dx, j + dy
                        # option2:  q1's neighbor as candidate
                        if (ii, jj) in q2:
                            return step + 1
                        if (ii, jj) not in vis and -1 <= ii <= x + 2 and -1 <= jj <= y + 2:
                            vis.add((ii, jj))
                            q1_nxt.add((ii, jj))
                q1 = q1_nxt
                step += 1
            return -1

        return fxr_bibfs()


sl = Solution()
print(sl.minKnightMoves(x=2, y=1))
print(sl.minKnightMoves(x=5, y=5))
