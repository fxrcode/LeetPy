"""
tag: medium, logic
Lookback:
* don't code before understand problem and clear logic
* piecewise analysis (#1093)
[ ] REDO
"""
from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def os():
            """
            Runtime: 50 ms, faster than 35.38% of Python3 online submissions for Valid Tic-Tac-Toe State.

            https://leetcode-cn.com/problems/valid-tic-tac-toe-state/solution/you-xiao-de-jing-zi-you-xi-by-leetcode-s-c1j3/
            """

            def win(p: str) -> bool:
                return (
                    any((board[i][0] == p and board[i][1] == p and board[i][2] == p) or (board[0][i] == p and board[1][i] == p and board[2][i] == p) for i in range(3))
                    or (board[0][0] == p and board[1][1] == p and board[2][2] == p)
                    or (board[0][2] == p and board[1][1] == p and board[2][0] == p)
                )

            oCount = sum(row.count("O") for row in board)
            xCount = sum(row.count("X") for row in board)
            # case 1: xCount must = oCount or oCount+1
            if oCount != xCount and oCount != xCount - 1:
                return False
            # case 2: if X win, must xCount = oCount +1
            if oCount != xCount - 1 and win("X"):
                return False
            # case 3: if O win, must xCount = oCount
            if oCount != xCount and win("O"):
                return False
            return True

        return os()

        def fxr_os():
            """
            https://leetcode-cn.com/problems/valid-tic-tac-toe-state/solution/you-xiao-de-jing-zi-you-xi-by-leetcode-s-c1j3/
            Runtime: 28 ms, faster than 96.13% of Python3 online submissions for Valid Tic-Tac-Toe State.

            referred os-cn

            """
            allsum = 0
            row = [0] * 3
            col = [0] * 3
            diag = antidiag = 0
            for r in range(len(board)):
                for c in range(len(board[0])):
                    play = 0
                    if board[r][c] == "X":
                        play = 1
                    elif board[r][c] == "O":
                        play = -1
                    row[r] += play
                    col[c] += play
                    if r == c:
                        diag += play
                    if r + c == len(board) - 1:
                        antidiag += play
                    allsum += play
            if not 0 <= allsum <= 1:
                return False

            states = [*row, *col, diag, antidiag]
            xwin = any(s == 3 for s in states)
            owin = any(s == -3 for s in states)
            if xwin == owin == True:
                return False
            if xwin:
                if allsum != 1:
                    return False
            if owin:
                if allsum != 0:
                    return False
            return True

        return fxr()


sl = Solution()
print(sl.validTicTacToe(board=["O  ", "   ", "   "]))
print(sl.validTicTacToe(board=["XOX", " X ", "   "]))
print(sl.validTicTacToe(board=["XOX", "O O", "XOX"]))
assert (sl.validTicTacToe(["XXX", "OOX", "OOX"])) == True
assert (sl.validTicTacToe(["XXX", "XOO", "OO "])) == False  # 105 / 109 test cases passed.
assert (sl.validTicTacToe(["XXO", "XOX", "OXO"])) == False  # 108 / 109 test cases passed.
