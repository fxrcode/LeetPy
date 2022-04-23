"""
Tag: Easy, BST
Lookback:
- This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
- AC in 5min
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def fxr():
            """
            Runtime: 26 ms, faster than 97.94% of Python3 online submissions for Minimum Distance Between BST Nodes.

            """
            mn = float("inf")
            prev = None

            def ino(T: TreeNode):
                if T:
                    ino(T.left)
                    nonlocal prev, mn
                    if prev:
                        mn = min(mn, T.val - prev.val)
                    prev = T
                    ino(T.right)

            ino(root)
            return mn
