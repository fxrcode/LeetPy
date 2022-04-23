"""
✅ GOOD DFS (simulation)
Tag: Medium, DFS
Lookback:
- I'm bit slow in understanding problem's rules
- NO Need to pre-compute the numbers table! we can do it in dfs.
- Crux: when to dfs, when to return?
    - if (i,j) has adjacent mines, mark it and directly return
    - ow, mark (i,j) as blank, then dfs(ni,nj)
    - no need of visited set, b/c board is updated
"""

from black import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def os():
            """
            Runtime: 209 ms, faster than 67.01% of Python3 online submissions for Minesweeper.
            https://leetcode.com/problems/minesweeper/discuss/362566/Clean-python-dfs-code
            """
            m, n = len(board), len(board[0])

            def valid(i, j):
                return 0 <= i < m and 0 <= j < n

            def reveal(i, j):
                # board is: M, E, B, 1~8, X
                if not valid(i, j) or board[i][j] != "E":
                    return
                # count (i,j)'s adjacent mines
                mines = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        ni, nj = i + dx, j + dy
                        if valid(ni, nj) and board[ni][nj] == "M":
                            mines += 1
                if mines:
                    board[i][j] = str(mines)
                    return
                else:
                    board[i][j] = "B"
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            reveal(i + dx, j + dy)

            x, y = click
            if board[x][y] == "M":
                board[x][y] = "X"
            elif board[x][y] == "E":
                reveal(x, y)
            return board

        return os()

        def fxr():
            """
            Runtime: 475 ms, faster than 5.06% of Python3 online submissions for Minesweeper.

            """
            # step 1: pre-compute numbers
            m, n = len(board), len(board[0])
            nums = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if board[i][j].isdigit():
                        nums[i][j] = board[i][j]
                    if board[i][j] == "M":
                        for dx in range(-1, 2):
                            for dy in range(-1, 2):
                                ni, nj = i + dx, j + dy
                                if not (0 <= ni < m and 0 <= nj < n):
                                    continue
                                if board[ni][nj] == "E":
                                    nums[ni][nj] = str(int(nums[ni][nj]) + 1)
            vis = set()

            def dfs(i, j):
                if board[i][j] == "M":
                    board[i][j] = "X"
                    return
                if nums[i][j] != 0:
                    board[i][j] = nums[i][j]
                    return
                board[i][j] = "B"
                vis.add((i, j))
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        ni, nj = i + dx, j + dy
                        if not (0 <= ni < m and 0 <= nj < n):
                            continue
                        if (ni, nj) in vis:
                            continue
                        if board[ni][nj] == "M":
                            continue
                        dfs(ni, nj)

            dfs(click[0], click[1])
            return board

        return fxr()


sl = Solution()
print(
    sl.updateBoard(
        [
            ["B", "B", "B", "B", "1", "M", "M", "E"],
            ["B", "B", "B", "B", "1", "4", "M", "E"],
            ["B", "B", "B", "B", "B", "3", "M", "E"],
            ["B", "B", "B", "B", "B", "2", "M", "E"],
            ["1", "2", "2", "1", "B", "1", "1", "1"],
            ["E", "M", "M", "1", "B", "B", "B", "B"],
            ["E", "E", "E", "2", "2", "2", "2", "1"],
            ["E", "E", "E", "E", "M", "M", "E", "M"],
        ],
        [7, 2],
    )
)

# expected
"""
[
    ["B", "B", "B", "B", "1", "M", "M", "E"],
    ["B", "B", "B", "B", "1", "4", "M", "E"],
    ["B", "B", "B", "B", "B", "3", "M", "E"],
    ["B", "B", "B", "B", "B", "2", "M", "E"],
    ["1", "2", "2", "1", "B", "1", "1", "1"],
    ["E", "M", "M", "1", "B", "B", "B", "B"],
    ["1", "2", "2", "2", "2", "2", "2", "1"],
    ["B", "B", "B", "1", "M", "M", "E", "M"],
]
"""
