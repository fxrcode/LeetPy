"""
https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/
Leetcode Explore: Binary Tree - Solve problem recursively

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.


"""
# Definition for a binary tree node.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Your runtime beats 85.75 % of python3 submissions.
        AC in 1st try.
        """

        def top_down(root: TreeNode, sum) -> bool:
            if not root:
                return False
            if not root.left and not root.right:
                return sum == root.val

            l = top_down(root.left, sum - root.val)
            r = top_down(root.right, sum - root.val)
            return l or r

        return top_down(root, targetSum)
