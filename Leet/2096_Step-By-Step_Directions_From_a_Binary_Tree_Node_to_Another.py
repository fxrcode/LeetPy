"""
Tag: Medium, DFS
Looback:
Weekly Contest 270 (Dec 4, 2021)
Q3: Medium
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections_votrubac(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        """
        Runtime: 628 ms, faster than 100.00% of Python3 online submissions for Step-By-Step Directions From a Binary Tree Node to Another.

        https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/discuss/1612105/3-Steps
        """

        def find(node: TreeNode, x, path):
            """
            Basic root to node path in DFS, notice the path is reverse order
            """
            if node.val == x:
                return True
            if node.left and find(node.left, x, path):
                path.append("L")
            elif node.right and find(node.right, x, path):
                path.append("R")
            return path

        def common_prefix():
            sp, dp = [], []
            find(root, startValue, sp)
            find(root, destValue, dp)
            print(sp, dp)

            while sp and dp and sp[-1] == dp[-1]:
                sp.pop()
                dp.pop()
            return "".join(["U"] * (len(sp)) + dp[::-1])

        return common_prefix()

    def getDirections_fxr(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # lca
        def _lca(root: TreeNode, p, q):
            """
            copied from lca
            """
            if not root:
                return None
            if root.val in {p, q}:
                return root
            l = _lca(root.left, p, q)
            r = _lca(root.right, p, q)
            return root if l and r else l or r

        def _path(node: TreeNode, arr, x):
            """
            Copied from geek4geeks
            """
            if not node:
                return False
            arr.append(node)
            if node.val == x:
                return True
            if _path(node.left, arr, x) or _path(node.right, arr, x):
                return True
            arr.pop()
            return False

        def dec(arr):
            ans = []
            pa = arr[0]
            for i in range(1, len(arr)):
                if pa.left == arr[i]:
                    ans.append("L")
                    pa = pa.left

                else:
                    ans.append("R")
                    pa = pa.right
            return ans

        # then find path from lca ot start, dest
        lca = _lca(root, startValue, destValue)
        lca_start = []
        lca_dest = []
        _path(lca, lca_start, startValue)
        _path(lca, lca_dest, destValue)

        ans = ["U"] * (len(lca_start) - 1) + dec(lca_dest)
        return ans
