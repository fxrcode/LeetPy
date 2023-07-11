"""
https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2804/
Leetcode explore Recursion II: Backtracking

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
"""


from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        Runtime: 104 ms, faster than 31.46% of Python3 online submissions for N-Queens II.

        AC in 1. But take too long time to make backtrack generalized without init 1st row's.
        """

        def draw(n, path):
            pass

        def backtrack(n, r, path: List[int], res: List[List[int]]):
            """
            Args:
                n: total n (constant)
                r: current row to concern
                path: previous rows placement
                res
            """

            def valid(r, c, path) -> bool:
                for x in range(len(path)):
                    y = path[x]
                    if y == c:
                        return False
                    if x - y == r - c or x + y == r + c:
                        return False
                return True

            if len(path) == n:
                res.append(list(path))
                # res[0] += 1
                return

            for c in range(n):
                # check row, check diagnol
                if valid(r, c, path):
                    path.append(c)
                    backtrack(n, r + 1, path, res)
                    path.pop()

                """
                # BUG: this doesn't work without init 1st row, because initially path = [], so will never recursion
                for x in range(len(path)):
                    y = path[x]
                    if y == c:
                        continue
                    if x-y == r-c or x+y == r+c:
                        continue
                    backtrack(n, r+1, path + [c], res)
                """

        res = []
        # res = [0]
        backtrack(n, 0, [], res)
        return res


sl = Solution()
print(sl.totalNQueens(4))
