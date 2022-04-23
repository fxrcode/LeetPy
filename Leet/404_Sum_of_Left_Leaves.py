"""
tag: easy, dfs
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def fxr():
            def dfs(r: TreeNode, isleft: bool) -> int:
                """
                Runtime: 32 ms, faster than 91.21% of Python3 online submissions for Sum of Left Leaves.

                AC in 1.
                """
                if not r:
                    return 0
                if not (r.left or r.right):
                    return r.val if isleft else 0

                return dfs(r.left, True) + dfs(r.right, False)

            return dfs(root, False)

        return fxr()
