"""
DFS tag (easy)
[ ] REDO
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        def post():
            def dfs(node: TreeNode):
                """
                Runtime: 52 ms, faster than 82.06% of Python3 online submissions for Find All The Lonely Nodes.

                XXX: pre-order DFS since we just need to know lonely info. Use ^ (means XOR) to test iff only one kid
                break down to sub-problems and use the return values
                """
                if not node:
                    return []

                # XXX: snippet check either kid exist
                if (not node.left) ^ (not node.right):
                    r = node.left or node.right
                    return [r.val] + dfs(r)
                return dfs(node.left) + dfs(node.right)

            return dfs(root)

        def fxr():
            def dfs(node, res):
                """
                Runtime: 81 ms, faster than 18.30% of Python3 online submissions for Find All The Lonely Nodes.

                XXX: I'm still weak in sub-problems DFS... Here's general non-return val DFS to traverse whole tree
                """
                if not node:
                    return
                dfs(node.left, res)
                dfs(node.right, res)
                if not node.left and not node.right:
                    return
                if not node.left or not node.right:
                    lonely = node.left or node.right
                    res.append(lonely.val)

            res = []
            dfs(root, res)
            return res
