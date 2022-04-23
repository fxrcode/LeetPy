"""
tag: hard, DFS, BST
Lookback:
- Now I learned BST trick: +/-INF to do post-order BST check
Similar:
* 333
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def fxr_333():
            """
            Runtime: 667 ms, faster than 36.38% of Python3 online submissions for Maximum Sum BST in Binary Tree.

            """
            mx_sum = 0

            def dfs(T: TreeNode):
                if not T:
                    return 0, float("inf"), float("-inf")
                l_sm, l_mn, l_mx = dfs(T.left)
                r_sm, r_mn, r_mx = dfs(T.right)
                nonlocal mx_sum
                if l_mx < T.val < r_mn:
                    sm = T.val + l_sm + r_sm
                    mx_sum = max(sm, mx_sum)
                    return sm, min(l_mn, T.val), max(r_mx, T.val)
                else:
                    sm = max(l_sm, r_sm)
                    mx_sum = max(sm, mx_sum)
                    return sm, float("-inf"), float("inf")

            dfs(root)
            return mx_sum
