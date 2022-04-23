"""
tag: medium, dfs
Lookback
- AC in 1. Obvious post-order DFS, so current node can compare with its children's sum. 
    * one caveat: what does dfs return? Ans: sum of subtree r!
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        def fxr():
            """
            Runtime: 1178 ms, faster than 46.29% of Python3 online submissions for Count Nodes Equal to Sum of Descendants.
            T: O(V)
            """
            cnt = 0

            def post(r: TreeNode) -> int:
                if not r:
                    return 0
                nonlocal cnt
                subsum = post(r.left) + post(r.right)
                cnt += subsum == r.val
                return subsum + r.val  # I forgot to add r.val in 1st try, so ALL 0.

            post(root)
            return cnt
