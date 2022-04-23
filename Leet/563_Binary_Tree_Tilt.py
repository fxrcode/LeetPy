'''
Daily Challenge (Dec 8)

'''
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def fx_dfs(node: TreeNode, res):
            """
            Runtime: 56 ms, faster than 79.09% of Python3 online submissions for Binary Tree Tilt.

            AC in 5min :)
            T: O(N) N=#nodes
            """
            if not node:
                return 0
            sum_l = fx_dfs(node.left, res)
            sum_r = fx_dfs(node.right, res)
            res[0] += abs(sum_l - sum_r)
            return sum_l + sum_r + node.val

        res = [0]
        fx_dfs(root, res)
        return res[0]
