"""
Tag: Easy, Skills, Simulation
Lookback:
- when move in direction, use DIR to loop!
"""

from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def lee215():
            """
            Runtime: 43 ms, faster than 56.03% of Python3 online submissions for Available Captures for Rook.

            https://leetcode.com/problems/available-captures-for-rook/discuss/242932/JavaC%2B%2BPython-Straight-Forward-Solution
            ! when move in direction, loop DIR
            """
            DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for i in range(8):
                for j in range(8):
                    if board[i][j] == "R":
                        x0, y0 = i, j
            res = 0
            for i, j in DIR:
                x, y = x0 + i, y0 + j
                while 0 <= x < 8 and 0 <= y < 8:
                    if board[x][y] == "p":
                        res += 1
                        break
                    if board[x][y] != ".":
                        break
                    x, y = x + i, y + j
            return res

        return lee215()

        def fxr():
            """
            Runtime: 56 ms, faster than 23.62% of Python3 online submissions for Available Captures for Rook.

            SO UGLY
            """

            def capture(i, j):
                cap = 0
                # row
                for r in range(i - 1, -1, -1):
                    if board[r][j] == "B":
                        break
                    elif board[r][j] == "p":
                        cap += 1
                        break
                for r in range(i + 1, m):
                    if board[r][j] == "B":
                        break
                    elif board[r][j] == "p":
                        cap += 1
                        break
                for c in range(j - 1, -1, -1):
                    if board[i][c] == "B":
                        break
                    elif board[i][c] == "p":
                        cap += 1
                        break
                for c in range(j + 1, n):
                    if board[i][c] == "B":
                        break
                    elif board[i][c] == "p":
                        cap += 1
                        break
                return cap

            m, n = len(board), len(board[0])
            rooks = []
            cnt = 0
            for r in range(m):
                for c in range(n):
                    if board[r][c] == "R":
                        rooks.append((r, c))

            for i, j in rooks:
                cnt += capture(i, j)
            return cnt

        return fxr()


sl = Solution()
board = [
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "p", ".", ".", ".", "."],
    [".", ".", ".", "R", ".", ".", ".", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "p", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
]
# board = [
#     [".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", "p", ".", ".", ".", "."],
#     [".", ".", ".", "p", ".", ".", ".", "."],
#     ["p", "p", ".", "R", ".", "p", "B", "."],
#     [".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", "B", ".", ".", ".", "."],
#     [".", ".", ".", "p", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", "."],
# ]
# board = [
#     [".", ".", ".", ".", ".", ".", ".", "."],
#     [".", "p", "p", "p", "p", "p", ".", "."],
#     [".", "p", "p", "B", "p", "p", ".", "."],
#     [".", "p", "B", "R", "B", "p", ".", "."],
#     [".", "p", "p", "B", "p", "p", ".", "."],
#     [".", "p", "p", "p", "p", "p", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", "."],
# ]
print(sl.numRookCaptures(board))
