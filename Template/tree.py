"""
手把手刷二叉树系列完结篇
后序位置的特殊之处

# two properties of Tree
* height
* depth
"""

from typing import Optional


class TreeNode:
    # Definition for a Node.
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def post(node):
            if not node:
                return 0
            return post(node.left) + post(node.right) + 1

        return post(root)

    def diameter(self, root: "TreeNode") -> int:
        def labuladong_post():
            """
            O(N)
            """
            ans = 0

            def post(node):
                if not node:
                    return 0
                max_l = post(node.left)
                max_r = post(node.right)
                cur_diam = max_l + max_r
                nonlocal ans
                ans = max(ans, cur_diam)
                return 1 + max(max_l, max_r)

        return labuladong_post()

    def invertTree(self, root: TreeNode) -> TreeNode:
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
