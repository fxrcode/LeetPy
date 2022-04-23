"""
每日一题打卡群 (12/8/2021)
"""
from typing import List, Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def clean_dfs():
            """
            show case pre/in/post order traversal in 1 problem~
            Runtime: 36 ms, faster than 96.96% of Python3 online submissions for Boundary of Binary Tree.

            https://leetcode.com/problems/boundary-of-binary-tree/discuss/101308/python-dfs-solution
            """

            def dfs_l(node):
                if not node or not node.left and not node.right:
                    return
                boundary.append(node.val)
                if node.left:
                    dfs_l(node.left)
                else:
                    dfs_l(node.right)

            def leaves(node):
                # why
                if not node:
                    return
                leaves(node.left)
                if node != root and not node.left and not node.right:
                    boundary.append(node.val)
                leaves(node.right)

            def dfs_r(node):
                if not node or not node.left and not node.right:
                    return
                if node.right:
                    dfs_r(node.right)
                else:
                    dfs_r(node.left)
                boundary.append(node.val)

            if not root:
                return []
            boundary = [root.val]
            dfs_l(root.left)
            leaves(root)
            dfs_r(root.right)
            return boundary

        def fxr():
            """
            Runtime: 60 ms, faster than 17.25% of Python3 online submissions for Boundary of Binary Tree.

            T: O(V+E)
            """
            if not root:
                return []
            lb, rb = [], []
            cur = root.left
            while cur:
                lb.append(cur.val)
                cur = cur.left if cur.left else cur.right
            lb = lb[:-1]

            cur = root.right
            while cur:
                rb.append(cur.val)
                cur = cur.right if cur.right else cur.left
            rb = rb[:-1]
            rb.reverse()

            leaves = []

            def dfs(node, ret):
                if not node:
                    return
                if not node.left and not node.right:
                    ret.append(node.val)
                dfs(node.left, ret)
                dfs(node.right, ret)

            if root.left or root.right:
                # say: Tree: [1], so no leaves!
                dfs(root, leaves)

            return [root.val] + lb + leaves + rb
