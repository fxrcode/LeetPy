"""
Weekly Contest 292 (May 7, 2022)
2/2
"""


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        DIR = {(0, 1), (1, 0)}
        m, n = len(grid), len(grid[0])

        def dfs(i, j, need) -> bool:
            if (i, j) == (m - 1, n - 1):
                return need == 1

            if grid[i][j] == "(":
                need += 1
            else:
                need -= 1
            ans = False
            for dx, dy in DIR:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    ans |= dfs(x, y, need)
            return ans

        if grid[m - 1][n - 1] != ")" or grid[0][0] != "(":
            return False
        return dfs(0, 0, 0)

    def countTexts(self, pressedKeys: str) -> int:
        four = "79"

        def bt(i, path, res):
            if i == len(pressedKeys):
                res[0] += 1
                return
            if pressedKeys[i] in four:
                for streak in range(1, 5):
                    if (
                        i + streak <= len(pressedKeys)
                        and len(set(pressedKeys[i : i + streak])) == 1
                    ):
                        bt(i + streak, path + [pressedKeys[i : i + streak]], res)
            else:
                for streak in range(1, 4):
                    if (
                        i + streak <= len(pressedKeys)
                        and len(set(pressedKeys[i : i + streak])) == 1
                    ):
                        bt(i + streak, path + [pressedKeys[i : i + streak]], res)

        res = [0]
        bt(0, [], res)
        return res[0] % (10**9 + 7)

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        cnt = 0

        def dfs(T: TreeNode):
            if not T:
                return 0, 0
            l, lc = dfs(T.left)
            r, rc = dfs(T.right)
            if (l + r + T.val) // (lc + rc + 1) == T.val:
                nonlocal cnt
                cnt += 1
            return l + r + T.val, lc + rc + 1

        dfs(root)
        return cnt

    def largestGoodInteger(self, num: str) -> str:
        mx = -1
        for i in range(len(num) - 2):
            n = num[i : i + 3]
            if len(set(n)) == 1:
                mx = max(mx, int(n[0]))
        return "".join(str(mx) * 3) if mx != -1 else ""


sl = Solution()
print(
    sl.hasValidPath(
        grid=[["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]]
    )
)
print(
    sl.hasValidPath(
        [
            ["(", "(", ")", "(", "(", ")", "(", ")", "("],
            [")", "(", "(", "(", ")", ")", ")", "(", "("],
            ["(", ")", ")", "(", "(", ")", "(", "(", "("],
            ["(", "(", ")", "(", ")", "(", "(", ")", "("],
            ["(", ")", "(", ")", ")", ")", "(", ")", ")"],
        ]
    )
)
# print(sl.countTexts(pressedKeys="2222"))
# print(sl.countTexts("22233"))
# print(sl.countTexts(pressedKeys="222222222222222222222222222222222222"))
# root = TreeNode(4, TreeNode(8, TreeNode(0), TreeNode(1)), TreeNode(5, None, TreeNode(6)))
# print(sl.averageOfSubtree(root))
# print(sl.largestGoodInteger(num="6777133339"))
# print(sl.largestGoodInteger(num="2300019"))
# print(sl.largestGoodInteger("42352338"))
# print(sl.largestGoodInteger("222"))
