"""
tag: Medium, DFS
Lookback:
- I can't bind my mind to use post-order, b/c I go for pre-order initially.
[ ] REDO (use post-order dfs)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def lee215():
            # Runtime: 273 ms, faster than 81.80% of Python3 online submissions for Count Good Nodes in Binary Tree.
            def post_dfs(T: TreeNode, mx):
                """
                post-order dfs: directly count good nodes in tree w/ root = T
                """
                if not T:
                    return 0
                res = 1 if T.val >= mx else 0
                mx = max(mx, T.val)
                # Divide
                l, r = post_dfs(T.left, mx), post_dfs(T.right, mx)
                # Conquer
                return res + l + r

            return post_dfs(root, -10000)

        def fxr():
            # Runtime: 307 ms, faster than 66.07% of Python3 online submissions for Count Good Nodes in Binary Tree.
            goods = []

            def pre_dfs(node: TreeNode, premax: int):
                """
                beginner dfs: pre-order, so I have to use global counter
                As labuladong: 2 type of dfs: enumerate whole tree (pre-order) vs D&C (post-order)
                """
                if not node:
                    return
                if premax <= node.val:
                    goods.append(node.val)
                for k in (node.left, node.right):
                    pre_dfs(k, max(premax, node.val))

            pre_dfs(root, float("-inf"))
            return len(goods)
