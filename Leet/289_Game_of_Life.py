"""
✅ GOOD Matrix (state: from 1bit => 2bit)
tag: Medium, Matrix
Lookback:
- Pochmann: state is bool, so we use 2-bit [new state, old state] to represent, so we can do the regular count, while get new state. And easy to get back to bool state in final result
- OS: Trick: define dummy state, so as to in-place next state. Then another O(N) to get real next state
- reminds #41.
"""

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def pochmann():
            """
            Since the board has ints but only the 1-bit is used, I use the 2-bit to store the new state. At the end, replace the old state with the new state by shifting all values one bit to the right.

            Runtime: 36 ms, faster than 85.68% of Python3 online submissions for Game of Life.
            """
            m, n = len(board), len(board[0])

            def cntNei(i, j):
                # for neighbors, no need range loop, simply directly get triples.
                # careful on check, b/c bit-2 is new state, bit-1 is old state.
                return sum(1 for x in (i - 1, i, i + 1) for y in (j - 1, j, j + 1) if 0 <= x < m and 0 <= y < n and board[x][y] & 1)

            # count neighbors
            for i in range(m):
                for j in range(n):
                    cnt = cntNei(i, j)
                    cnt -= board[i][j]  # because we included the cell in the neighbors count
                    print(i, j, cnt)
                    if cnt == 3 or (cnt == 2 and board[i][j] == 1):  # live conditions
                        board[i][j] |= 2  # equivalent to board[i][j] |= 1<<1 --- set the 2nd bit which is the next set

            # convert back
            for i in range(m):
                for j in range(n):
                    board[i][j] >>= 1
            print(board)

        return pochmann()

        def os_o1m():
            """
            Runtime: 33 ms, faster than 88.84% of Python3 online submissions for Game of Life.

            Follow-up: board can be inf, how to calc next state in-place w/ O(1) memory?
            XXX: define dummy states: 1->0 (-1) 0->1 (2)
            """

            def cnt(i, j):
                ones = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        x, y = i + dx, j + dy
                        if (x, y) == (i, j):
                            continue
                        if 0 <= x < m and 0 <= y < n and abs(board[x][y]) == 1:
                            ones += 1
                return ones

            m, n = len(board), len(board[0])
            for i in range(m):
                for j in range(n):
                    ones = cnt(i, j)
                    if board[i][j] == 1:
                        if ones < 2:
                            board[i][j] = -1
                        elif 2 <= ones <= 3:
                            board[i][j] = 1
                        else:
                            board[i][j] = -1
                    else:
                        if ones == 3:
                            board[i][j] = 2

            for i in range(m):
                for j in range(n):
                    if board[i][j] == -1:
                        board[i][j] = 0
                    if board[i][j] == 2:
                        board[i][j] = 1
            return board

        # return os_o1m()

        def fxr():
            """
            Runtime: 32 ms, faster than 94.80% of Python3 online submissions for Game of Life.

            XXX: how to copy matrix?
            """

            def cnt(i, j):
                ones = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        x, y = i + dx, j + dy
                        if (x, y) == (i, j):
                            continue
                        if 0 <= x < m and 0 <= y < n:
                            ones += copy_board[x][y]
                return ones

            m, n = len(board), len(board[0])
            copy_board = [[board[r][c] for c in range(n)] for r in range(m)]
            for i in range(m):
                for j in range(n):
                    ones = cnt(i, j)
                    # print(i, j, ones)
                    if copy_board[i][j] == 1:
                        if ones < 2:
                            board[i][j] = 0
                        elif 2 <= ones <= 3:
                            board[i][j] = 1
                        else:
                            board[i][j] = 0
                    else:
                        if ones == 3:
                            board[i][j] = 1
            return board

        return fxr()


sl = Solution()
print(sl.gameOfLife(board=[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
# print(sl.gameOfLife(board=[[1, 1], [1, 0]]))
