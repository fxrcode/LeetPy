"""
https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1373/
Leetcode explore Queue & Stack
You are given an m x n grid rooms initialized with these three possible values.
"""


from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Your runtime beats 41.24 % of python3 submissions.

        """

        def flood_fill():
            """
            Runtime: 490 ms, faster than 22.09% of Python3 online submissions for Walls and Gates.

            XXX: no need of visited given empty room = INF, no need of step, or level order loop.
            """
            DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            R, C = len(rooms), len(rooms[0])
            q = deque([(r, c) for r in range(R) for c in range(C) if rooms[r][c] == 0])
            while q:
                r, c = q.popleft()
                for dx, dy in DIR:
                    xx, yy = r + dx, c + dy
                    if 0 <= xx < R and 0 <= yy < C and rooms[xx][yy] > 2**30:
                        rooms[xx][yy] = rooms[r][c] + 1
                        q.append((xx, yy))

        def fxr():
            """
            XXX: In fact, I'm still not quite sure if it works because I just memoized BFS template,
                but not fully understand in mind.
            Note: every for _ in range(qlen) are in same level!
            """
            DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            R, C = len(rooms), len(rooms[0])
            gates = [(r, c) for r in range(R) for c in range(C) if rooms[r][c] == 0]
            q = deque(gates)
            visited = set(gates)
            step = 1
            while q:
                qlen = len(q)

                for _ in range(qlen):
                    x, y = q.popleft()
                    # update room and skip wall
                    for dx, dy in DIR:
                        xx, yy = x + dx, y + dy
                        if 0 <= xx < R and 0 <= yy < C:
                            if rooms[xx][yy] == -1 or (xx, yy) in visited:
                                continue
                            rooms[xx][yy] = step
                            q.append((xx, yy))
                            visited.add((xx, yy))
                step += 1
