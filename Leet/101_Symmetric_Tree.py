"""
https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/534/
Leetcode Explore: Binary Tree - Solve problem recursively

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Your runtime beats 84.78 % of python3 submissions.
        XXX: simple generic way to convert recursive to iterative using stack:
        if you have more than one recursive call inside and you want to preserve the order of the calls,
        you have to add them in the reverse order to the stack
        """

        def iter(root: TreeNode) -> bool:
            if not root:
                return True
            stk = [root.left, root.right]
            while stk:
                right = stk.pop()
                left = stk.pop()
                if not left and not right:
                    continue
                if not left or not right or right.val != left.val:
                    return False
                # notice the order we push is EXACTLY reverse of multiple recursive calls
                stk.append(right.left)
                stk.append(left.right)
                stk.append(right.right)
                stk.append(left.left)
            return True

        def dfs_td(left: TreeNode, right: TreeNode) -> bool:
            """
            Your runtime beats 95.35 % of python3 submissions.
            XXX: exactly follow the definition of symmetric recursively
            """
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val == right.val:
                return dfs_td(left.left, right.right) and dfs_td(left.right, right.left)
            return False

        if not root:
            return True

        return dfs_td(root, root)
