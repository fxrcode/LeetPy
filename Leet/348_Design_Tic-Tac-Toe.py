"""
Amazon Top50
tag: medium
"""
P1, P2 = 1, -1


class TicTacToe:
    """
    Runtime: 92 ms, faster than 62.57% of Python3 online submissions for Design Tic-Tac-Toe.

    """

    def __init__(self, n: int):
        self.R = [0] * n
        self.C = [0] * n
        self.D = 0
        self.AD = 0
        self.N = n

    def move(self, row: int, col: int, player: int) -> int:
        p = 1 if player == 1 else -1

        self.R[row] += p
        self.C[col] += p
        if row == col:
            self.AD += p
        if row + col == self.N - 1:
            self.D += p
        if (
            abs(self.R[row]) == self.N
            or abs(self.C[col]) == self.N
            or abs(self.D) == self.N
            or abs(self.AD) == self.N
        ):
            return player
        return 0
