"""
Tag: Medium, BST, DFS
Lookback:
- for placeholder empty or valid process, can unified as mono-stack or interval merge
- early termination learned from Labuladong
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Runtime: 77 ms, faster than 81.92% of Python3 online submissions for Recover Binary Search Tree.

        Do not return anything, modify root in-place instead.
        """

        def ino(T: TreeNode) -> bool:
            if not T:
                return False
            nonlocal x, y, pre
            if ino(T.left):
                return True
            if pre and pre.val > T.val:
                y = T
                if not x:
                    x = pre
                else:
                    # BUG: y = T. eg2: 1,3,2,4
                    return True
            pre = T
            if ino(T.right):
                return True

        x = y = pre = None
        ino(root)
        x.val, y.val = y.val, x.val
