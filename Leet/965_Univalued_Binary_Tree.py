"""
🌸Huahua Tree List (type: 100. Same Tree)
"""


from typing import Optional


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def os(node):
            """
            Runtime: 32 ms, faster than 64.22% of Python3 online submissions for Univalued Binary Tree.

            pre-order DFS, so stop early once detect not match, so prevent child recursion
            """
            if not node:
                return True
            if node.left:
                if node.left.val != node.val:
                    return False
            if node.right:
                if node.right.val != node.val:
                    return False
            return os(node.left) and os(node.right)

        def fxr_dfs(node):
            """
            Your runtime beats 23.33 % of python3 submissions.

            !BAD: post-order DFS, so wasting time doing child recursion!!!
            """
            if not node:
                return True
            l, r = fxr_dfs(node.left), fxr_dfs(node.right)
            if not (l and r):
                return False
            bl = True

            if node.left:
                bl &= node.left.val == node.val
            if node.right:
                bl &= node.right.val == node.val
            return bl

        return fxr_dfs(root)
