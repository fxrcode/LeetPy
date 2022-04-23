"""
tag: easy, dfs
Lookback
- dfs needs more practice
    - DP, backtrack, logic problems...
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        Runtime: 33 ms, faster than 85.03% of Python3 online submissions for Binary Tree Paths.
        https://leetcode.com/problems/binary-tree-paths/discuss/68364/4-lines-python-DFS
        """

        def dfs(r: TreeNode, path):
            if r:
                path += str(r.val)
                if not (r.left or r.right):
                    res.append(path)
                    # return
                else:
                    path += "->"  # path is str, no need to backtrack
                    dfs(r.left, path)
                    dfs(r.right, path)

            res = []
            dfs(root, "")
            return res

        return dfs(root)

    def binaryTreePaths_fxr(self, root: Optional[TreeNode]) -> List[str]:
        """
        Runtime: 28 ms, faster than 90.91% of Python3 online submissions for Binary Tree Paths.

        """

        def bt(r: TreeNode, path, res):
            if not r:
                return
            if not r.left and not r.right:
                res.append("->".join(path))
                return
            for n in {r.left, r.right}:
                if n:
                    path.append(str(n.val))
                    bt(n, path, res)
                    path.pop()  # path is mutable (list)

        res = []
        bt(root, [str(root.val)], res)
        return res
