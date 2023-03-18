"""
date: 03132023
Tag: Medium, DFS
Lookback: need more practice on DFS 230+ problems
[ ] TODO: iterative impl
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def fxr_predfs():
            """
            Runtime: 52 ms, faster than 28.65% of Python3 online submissions for Sum Root to Leaf Numbers.

            XXX:
            """

            def dfs(r: TreeNode, presum: int) -> int:
                if not r:
                    # XXX: must handle None node, ow, it failed tree: [0,1] for int+NoneType...
                    return 0

                presum = presum * 10 + r.val
                if not r.left and not r.right:
                    return presum

                return dfs(r.left, presum) + dfs(r.right, presum)

            return dfs(root, 0)

        return fxr_predfs()
