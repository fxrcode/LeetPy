"""
https://leetcode.com/company/google/
Easy

Lookback: Cool logic to check if row/col/diag/antidiag win by marking player1=1, player2=-1, and runtime sum row/col/diag/anti-diagonal
"""


from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def os_runtime_sum():
            """
            Runtime: 28 ms, faster than 90.67% of Python3 online submissions for Find Winner on a Tic Tac Toe Game.

            n = len(board), m = len(moves)
            T: O(m), M: O(n)
            """
            n = 3
            rows = [0] * n
            cols = [0] * n
            diag, anti = 0, 0
            player = 1

            for r, c in moves:
                # update rows/cols/diag/anti
                rows[r] += player
                cols[c] += player
                if r == c:
                    diag += player
                if r + c == n - 1:
                    anti += player

                # check if win
                if any(abs(line) == n for line in (rows[r], cols[c], diag, anti)):
                    return "A" if player == 1 else "B"
                # switch player
                player *= -1
            return "Draw" if len(moves) == n**2 else "Pending"

        def fxr_brute():
            """
            Runtime: 32 ms, faster than 74.34% of Python3 online submissions for Find Winner on a Tic Tac Toe Game.

            metacognition:
            case analysis
            if full moves: A: 5 moves, B: 4 moves. and no win => draw
            if not full moves, and no win => pending

            for all subset len=3 of A or B, check if middle move is half of sum(1st+3rd) move.
            Since max n = 5, so C(5,3) => 10.

            """

            def win(mvs):
                n = len(mvs)
                for i in range(n - 3 + 1):
                    for j in range(i + 1, n - 2 + 1):
                        for k in range(j + 1, n):
                            tmp = [mvs[i], mvs[j], mvs[k]]
                            tmp.sort(key=lambda co: (co[0], co[1]))
                            if tmp[1][0] * 2 == (tmp[0][0] + tmp[2][0]) and tmp[1][
                                1
                            ] * 2 == (tmp[0][1] + tmp[2][1]):
                                return True
                return False

            A, B = [], []
            a = True
            for move in moves:
                if a:
                    A.append(move)
                else:
                    B.append(move)
                a = not a
            la, lb = len(A), len(B)
            if la < 3:
                return "Pending"
            if win(A):
                return "A"
            if win(B):
                return "B"
            if la == 5:
                return "Draw"
            return "Pending"

        return fxr_brute()


sl = Solution()
print(sl.tictactoe([[1, 2], [2, 1], [1, 0], [0, 0], [0, 1], [2, 0], [1, 1]]))
