"""
https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

TODO [ ] iterative
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(r: TreeNode) -> TreeNode:
            """
            Runtime: 57 ms, faster than 16.45% of Python3 online submissions for Invert Binary Tree.

            """
            if not r:
                return None
            r.left, r.right = dfs(r.right), dfs(r.left)
            return r

        def iter():
            """
            Runtime: 52 ms, faster than 18.29% of Python3 online submissions for Invert Binary Tree.

            REF: https://labuladong.github.io/algo/2/18/33/
            """
            stk, visited = [], TreeNode(None)

            def pushleftbranch(r: TreeNode):
                while r:
                    # preorder
                    r.left, r.right = r.right, r.left
                    stk.append(r)
                    r = r.left

            pushleftbranch(root)
            while stk:
                p = stk[-1]
                # p.left subtree done, but p.right not
                if (not p.left or p.left == visited) and p.right != visited:
                    # inorder
                    pushleftbranch(p.right)
                # p.right subtree done
                if not p.right or p.right == visited:
                    # postorder
                    visited = stk.pop()
