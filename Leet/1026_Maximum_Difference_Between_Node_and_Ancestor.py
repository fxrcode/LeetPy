"""
LOOKBACK: if ask for max diff, we just need to compare v with min/max from root to this node
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def os_minmax():
            """
            Runtime: 50 ms, faster than 21.75% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
            * same to 98. Validate Binary Search Tree

            T: O(N)
            """

            def dfs(node, mn, mx):
                """
                Find the mn,mx in the path from root to this node
                Then return mx-mn at leaf
                """
                if not node:
                    return mx - mn
                mn = max(mn, node.val)
                mx = min(mx, node.val)
                return max(dfs(node.left, mn, mx), dfs(node.right, mn, mx))

            return dfs(root, root.val, root.val)

        def fxr_2layer():
            """
            Runtime: 6348 ms, faster than 5.08% of Python3 online submissions for Maximum Difference Between Node and Ancestor.

            T: O(N^2)
            """

            def mxdfs(node, v, mx):
                if not node:
                    return
                mx[0] = max(mx[0], abs(node.val - v))
                mxdfs(node.left, v, mx)
                mxdfs(node.right, v, mx)

            def dfs(node, mx):
                if not node:
                    return
                mxdfs(node, node.val, mx)
                dfs(node.left, mx)
                dfs(node.right, mx)

            mx = [0]
            dfs(root, mx)
            return mx[0]

        return fxr_2layer()
