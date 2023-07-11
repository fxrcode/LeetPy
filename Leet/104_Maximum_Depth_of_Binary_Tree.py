"""
✅ GOOD Tree (TD vs BU)
Daily Challenge (Feb 13, 2022)
手把手刷二叉树系列完结篇

https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/535/
Leetcode Explore: Binary Tree - Solve problem recursively
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2375/
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bottom_up(r: TreeNode) -> int:
            """
            Your runtime beats 49.98 % of python3 submissions.

            Q: When to use Bottom-up approach?
                * Ask youself 1 question: if you know the answer of its children, can you calculate the answer of that node?

            XXX: Common snippet.
            """
            if not r:
                return 0

            return max(self.maxDepth(r.left), self.maxDepth(r.right)) + 1

        # global var for top-down recursive
        ans = 0

        def top_down(r: TreeNode, depth: int) -> None:
            """
            Runtime: 60 ms, faster than 21.26% of Python3 online submissions for Maximum Depth of Binary Tree.
            Q: When to use Top-down approach?
                * Ask youself 2 questions, if both yes, then you can use TD
                1. can you determine some params to help the node know its answer?
                2. can you use these params and the value of the node itself to determine what should be the params passed to its child?
            """
            if not r:
                return
            if not r.left and not r.right:
                nonlocal ans
                ans = max(ans, depth)
            if r.left:
                top_down(r.left, depth + 1)
            if r.right:
                top_down(r.right, depth + 1)

        return bottom_up(root)

    def maxDepth_labuladong(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 78 ms, faster than 5.27% of Python3 online submissions for Maximum Depth of Binary Tree.

        """
        res, depth = 0, 0

        def max_depth(root):
            def traverse(node):
                nonlocal res, depth

                if not node:
                    res = max(res, depth)
                    return
                depth += 1
                traverse(node.left)
                traverse(node.right)
                depth -= 1

            traverse(root)
            return res

        return max_depth(root)


sl = Solution()
root = TreeNode(
    3, left=TreeNode(8), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))
)
sl.maxDepth_labuladong(root)
