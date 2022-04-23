"""
✅ GOOD DFS (Tree modify)
🌸 Huahua Tree List
tag: medium, dfs
Lookback:

[ ] REDO
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def prune(node):
            """
            Runtime: 33 ms, faster than 32.39% of Python3 online submissions for Binary Tree Pruning.

            !lee215
            XXX: My rule is that, If you don't new it, don't delete it.
            """
            if not node:
                return None
            node.left = prune(node.left)
            node.right = prune(node.right)
            if not node.left and not node.right and node.val == 0:
                return None
            return node

        def contains1(node):
            """
            Runtime: 28 ms, faster than 87.55% of Python3 online submissions for Binary Tree Pruning.

            WA: 18 / 30 test cases passed.
            [0,null,0,0,0]
            """
            if not node:
                return False

            if node.left == node.right == None:
                return node.val == 1

            l, r = contains1(node.left), contains1(node.right)
            if not l:
                node.left = None
            if not r:
                node.right = None
            if not l and not r and node.val == 0:
                return False
            return True

        # return root if contains1(root) else None
        return prune(root)
