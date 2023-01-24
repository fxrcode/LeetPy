"""
✅ GOOD BFS (indexing)
tag: Medium, BFS, Matrix
date: 01242023
takeaway:
Amazon Top50
"""

from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def lee215():
            """
            Runtime: 158 ms, faster than 51.68% of Python3 online submissions for Snakes and Ladders.

            """
            n = len(board)
            need = {1: 0}
            bfs = [1]
            for x in bfs:
                for i in range(x + 1, x + 7):
                    a, b = divmod(i - 1, n)
                    nxt = board[~a][b if a % 2 == 0 else ~b]
                    if nxt > 0:
                        i = nxt
                    if i == n * n:
                        return need[x] + 1
                    if i not in need:
                        need[i] = need[x] + 1
                        bfs.append(i)
            return -1

        # return lee215()

        def fxr_bfs():
            """
            Runtime: 188 ms, faster than 36.82% of Python3 online submissions for Snakes and Ladders.

            T: O(N^2)
            """
            n = len(board)
            start = (1, 0)
            vis = set([1])
            q = deque([start])

            def toRC(pos):
                r, c = divmod(pos - 1, n)
                return ~r, c if r % 2 == 0 else ~c

            while q:
                pos, stp = q.popleft()
                if pos == n * n:
                    return stp
                for pp in range(pos + 1, pos + 7):
                    if pp > n * n:
                        continue
                    r, c = toRC(pp)
                    nxt = board[r][c]
                    if nxt > 0:
                        pp = nxt
                    if pp not in vis:
                        q.append((pp, stp + 1))
                        vis.add(pp)
            return -1

        return fxr_bfs()


sl = Solution()
# board = [[-1, -1], [-1, 3]]
# board = [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1],
#          [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
#          [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]
# board = [[-1, -1, 19, 10, -1], [2, -1, -1, 6, -1], [-1, 17, -1, 19, -1],
#          [25, -1, 20, -1, -1], [-1, -1, -1, -1, 15]]
board = [
    [-1, -1, -1, 46, 47, -1, -1, -1],
    [51, -1, -1, 63, -1, 31, 21, -1],
    [-1, -1, 26, -1, -1, 38, -1, -1],
    [-1, -1, 11, -1, 14, 23, 56, 57],
    [11, -1, -1, -1, 49, 36, -1, 48],
    [-1, -1, -1, 33, 56, -1, 57, 21],
    [-1, -1, -1, -1, -1, -1, 2, -1],
    [-1, -1, -1, 8, 3, -1, 6, 56],
]
print(sl.snakesAndLadders(board))
