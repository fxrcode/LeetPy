'''
https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2796/
Leetcode explore Recursion II: Backtracking

Write a program to solve a Sudoku puzzle by filling the empty cells.
'''


from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Labuladong ch 4.2
        Your runtime beats 21.83 % of python3 submissions.

        T: O(9^D), D is number of '.' in board

        """
        def draw(board):
            for r in board:
                print(r)
            print()

        def is_valid(board, r, c, n) -> bool:
            for i in range(9):
                if n == board[r][i]:
                    return False
                if n == board[i][c]:
                    return False
                # XXX: memoize this trick for box, notice i//3 vs i%3!
                if n == board[r//3*3+i//3][c//3*3+i % 3]:
                    return False
            return True

        '''
        def is_valid_WRONG(board, r, c, cand):
            for i in range(9):
                if board[r][i] == cand:
                    return False
                if board[i][c] == cand:
                    return False
                if board[r//3*3+i//3][c//3*3+i % 3] == cand:
                    return False
                # BUG: because this return True inside loooop!!!
                return True
        '''

        def bt(board, i, j) -> bool:
            """
            let recursion return bool, so as to exit recursion ASAP we got a solution
            """
            m, n = 9, 9
            # print(i, j)
            if j == n:
                # try next row
                return bt(board, i+1, 0)
            if i == m:
                draw(board)
                return True
            if board[i][j] != '.':
                # skip this
                return bt(board, i, j+1)
            for ch in map(str, range(1, 10)):
                if not is_valid(board, i, j, ch):
                    continue
                board[i][j] = ch
                if bt(board, i, j+1):
                    return True
                board[i][j] = '.'
            # XXX: no solution for r,c with any 1~9, so previous loc is not correct,
            # need to backtrack to try another num!
            return False

        print(bt(board, 0, 0))

    def solveSudoku_fxr_INFIN(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def draw(board):
            for r in board:
                print(r, end='')
            print()

        def all_filled(board) -> bool:
            for r in range(len(board)):
                for c in range(len(board[0])):
                    if board[r][c] == '.':
                        return False
            return True

        def is_valid(board, r, c, v) -> bool:
            if board[r][c] != '.':
                return False
            if v in board[r]:
                return False
            row = []
            for i in range(len(board[0])):
                b = board[r][i]
                if b != '.':
                    row.append(b)
            if len(row) != len(set(row)):
                return False
            # if len(board[r]) != len(set(board[r])):
            #     return False
            col = []
            for i in range(len(board)):
                b = board[i][c]
                if b != '.':
                    col.append(b)
            if len(col) != len(set(col)):
                return False
            if v in col:
                return False

            sub = (r//3, c//3)
            subm = []
            for i in range(sub[0], sub[0]+3):
                for j in range(sub[1], sub[1]+3):
                    b = board[i][j]
                    if b != '.':
                        subm.append(b)
            if len(subm) != len(set(subm)):
                return False
            if v in subm:
                return False
            return True

        def bt(board, res) -> None:
            if all_filled(board):
                res.append(list(board))
                return

            for x in range(len(board)):
                for y in range(len(board[0])):
                    for v in '123456789':
                        if is_valid(board, x, y, v):
                            board[x][y] = v
                            bt(board, res)
                            board[x][y] = '.'

        res = []
        bt(board, res)
        # draw(res[0])


# https://cs.stanford.edu/people/nick/py/python-map-lambda.html
# one_to_nine = list(map(str, range(1, 10)))
# print(one_to_nine)

sl = Solution()
sl.solveSudoku(board=[["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
               "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
