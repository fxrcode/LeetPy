"""
Tag: Easy
Lookback:
- this is what lee215/larry/rock/DBabichev feel about HARD problems.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        def fxr():
            return root.val == sum(root.left.val, root.right.val)
