'''
Daily Challenge (Nov 1)

'''
from typing import List
DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def labuladong():
            """
            Runtime: 128 ms, faster than 96.14% of Python3 online submissions for Surrounded Regions.

            """
            rows = len(board)
            cols = len(board[0])

            def dfs(row, col):
                board[row][col] = "Z"
                for dr, dc in (-1, 0), (0, 1), (1, 0), (0, -1):
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or board[nr][nc] != 'O':
                        continue
                    dfs(nr, nc)

            def flip():
                for row in range(rows):
                    for col in range(cols):
                        if board[row][col] == "Z":
                            board[row][col] = "O"
                        elif board[row][col] == "O":
                            board[row][col] = "X"

            for row in [0, rows - 1]:
                for col in range(cols):
                    if board[row][col] == 'O':
                        dfs(row, col)

            for col in [0, cols - 1]:
                for row in range(1, rows - 1):
                    if board[row][col] == 'O':
                        dfs(row, col)

            flip()

        def fxr_WA():
            """
            WA: 25/58 test cases passed
            case a: [["O","O","O"],["O","O","O"],["O","O","O"]]
            case b: [["X","O","X"],["X","O","X"],["X","O","X"]]
            """
            m, n = len(board), len(board[0])

            def dfs(i, j):
                print('dfs', i, j)
                if board[i][j] == 'X':
                    return
                flip = False
                for dx, dy in DIR:
                    ii, jj = i+dx, j+dy
                    if 0 <= ii < m and 0 <= jj < n and board[ii][jj] == 'X':
                        flip = True
                        break
                if flip:
                    board[i][j] = 'X'
                else:
                    return
                for dx, dy in DIR:
                    x, y = i+dx, j+dy
                    if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                        dfs(x, y)

            for i in range(1, m-1):
                for j in range(1, n-1):
                    if board[i][j] == 'O':
                        dfs(i, j)
