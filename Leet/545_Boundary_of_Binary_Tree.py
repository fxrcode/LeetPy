"""
✅ GOOD DFS (Tree)
Tag: Medium, DFS
Lookback:
- 每日一题打卡群 (12/8/2021)
- use pre/in/post order DFS in 1 problem!
[ ] REDO

"""
from collections import defaultdict
from typing import List, Optional


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
            Runtime: 48 ms, faster than 89.80% of Python3 online submissions for Boundary of Binary Tree.

            https://leetcode.com/problems/boundary-of-binary-tree/discuss/101308/python-dfs-solution
            """

            def dfs_l(T: TreeNode):
                if not T or not T.left and not T.right:
                    return
                boundary.append(T.val)
                if T.left:
                    dfs_l(T.left)
                else:
                    dfs_l(T.right)

            def leaves(T: TreeNode):
                # why
                if not T:
                    return
                leaves(T.left)
                if T != root and not T.left and not T.right:
                    boundary.append(T.val)
                leaves(T.right)

            def dfs_r(T: TreeNode):
                if not T or not T.left and not T.right:
                    return
                if T.right:
                    dfs_r(T.right)
                else:
                    dfs_r(T.left)
                boundary.append(T.val)

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

            def dfs(T: TreeNode, res):
                if not T:
                    return
                if not T.left and not T.right:
                    res.append(T.val)
                dfs(T.left, res)
                dfs(T.right, res)

            if root.left or root.right:
                # say: Tree: [1], so no leaves!
                dfs(root, leaves)

            return [root.val] + lb + leaves + rb
