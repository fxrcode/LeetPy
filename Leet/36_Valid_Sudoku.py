'''
https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1126/
Leetcode Explore: Hash Table. Practical Application - Design the Key
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:


'''


from typing import List


class Solution:
    def isValidSudoku_forum_clue(self, board: List[List[str]]) -> bool:
        """
        Runtime: 96 ms, faster than 72.59% of Python3 online submissions for Valid Sudoku.

        https://leetcode.com/problems/valid-sudoku/discuss/15451/A-readable-Python-solution

        XXX: clean and nice! I learned these:
            1. check unique with len(set) == len(). It's so common just like reverse linked list, floyd cycle, etc.
            2. finally memorize how nested list comprehension works, eg. loop box in sudoku
            3. transpost matrix by zip(*matrix), because zip() is like k-merge! and *() unpack matrix into rows.
        """
        def _valid_unit(box: List[List[str]]) -> bool:
            # helper function
            unit = [i for i in box if i != '.']
            # check if all unique is basic skill as reverse linked list
            return len(set(unit)) == len(unit)

        def check_row(board):
            # XXX: nice loop row by its naming!
            for row in board:
                if not _valid_unit(row):
                    return False
            return True

        def check_col(board):
            # XXX: zip and * ==> transpose matrix!
            for col in zip(*board):
                if not _valid_unit(col):
                    return False
            return True

        def check_box(board):
            # XXX: loop box left-up cornor
            for r in (0, 3, 6):
                for c in (0, 3, 6):
                    # XXX: nested list comprehension is easy, just same way we write regular loop, just move element logic from inner to loop to front of list!
                    box = [board[x][y]
                           for x in range(r, r+3) for y in range(c, c+3)]
                    if not _valid_unit(box):
                        return False
            return True

        return check_row(board) and check_col(board) and check_box(board)

    def isValidSudoku_fxr(self, board: List[List[str]]) -> bool:
        """
        Your runtime beats 8.50 % of python3 submissions.
        AC in 1 but so slooooooooooow!
        """
        def check_and_set(dic, r, c):
            if not board[r][c].isdigit():
                return True
            v = int(board[r][c])-1
            if dic[v] == 1:
                return False
            else:
                dic[v] = 1
            return True

        def clear_dic(dic):
            for i in range(9):
                dic[i] = 0

        row = [0 for _ in range(9)]
        col = [0 for _ in range(9)]
        box = [0 for _ in range(9)]

        # check 9 rows
        for r in range(9):
            for c in range(9):
                if not check_and_set(row, r, c):
                    return False
            clear_dic(row)
        # check 9 cols
        for c in range(9):
            for r in range(9):
                if not check_and_set(col, r, c):
                    return False
            clear_dic(col)

        binner = [[1, 1], [1, 4], [1, 7], [4, 1], [
            4, 4], [4, 7], [7, 1], [7, 4], [7, 7]]
        boxdir = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                  (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        # check 9 box
        for x, y in binner:
            for dx, dy in boxdir:
                if not check_and_set(box, x+dx, y+dy):
                    return False
            clear_dic(box)
        return True


sl = Solution()
board = \
    [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board1 = \
    [["8", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(sl.isValidSudoku_forum_clue(board1))
