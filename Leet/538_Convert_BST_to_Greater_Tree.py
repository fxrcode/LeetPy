"""
Tag: Medium, BST, DFS
Lookback:
Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def fxr():
            """
            Runtime: 80 ms, faster than 95.47% of Python3 online submissions for Convert BST to Greater Tree.
            """

            def ino(T: TreeNode, sumTillNow):
                if T:
                    ino(T.right, sumTillNow)
                    T.val += sumTillNow[0]
                    sumTillNow[0] = T.val
                    ino(T.left, sumTillNow)

            ino(root, [0])
            return root
