"""
https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

"""
# Definition for a binary tree node.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        def dfs(root1: TreeNode, root2: TreeNode) -> TreeNode:
            """
            Runtime: 84 ms, faster than 85.11% of Python3 online submissions for Merge Two Binary Trees.

            AC in 1.
            """
            # base
            """
            XXX: fxr is not elegant here
            if not root1 and not root2:
                return None

            if not root1 or not root2:
                return root1 or root2
            """
            if not root1:
                return root2
            if not root2:
                return root1

            # recur relation
            l = dfs(root1.left, root2.left)
            r = dfs(root1.right, root2.right)

            vl = root1.val if root1 else 0
            vr = root2.val if root2 else 0
            new_root = TreeNode(vl + vr)
            new_root.left, new_root.right = l, r
            return new_root

        return dfs(root1, root2)
