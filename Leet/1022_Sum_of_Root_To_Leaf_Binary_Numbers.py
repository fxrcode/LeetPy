"""
✅ GOOD DFS

Daily Challenge (Jan 11)
Tag: easy, DFS

Lookback:
+ Better understand DFS
+ preorder recursive, iterative, Enumeration (os) vs Divide&Conquer (lee215).

[ ] REDO
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def lee215_dp():
            """
            Divide & conquer recursion
            """

            def dp(r, val):
                if not r:
                    return 0
                val = val * 2 + r.val
                return dp(r.left, val) + dp(r.right, val)

            return dp(root, 0)

        def os_recur():
            """
            Runtime: 28 ms, faster than 97.35% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.

            T: O(N)
            """

            def preorder(r: TreeNode, cur_num):
                nonlocal root_to_leaf
                # XXX: snippet: check if leaf node
                if r:
                    cur_num = (cur_num << 1) | r.val
                    if not (r.left or r.right):
                        root_to_leaf += cur_num
                    preorder(r.left, cur_num)
                    preorder(r.right, cur_num)

            root_to_leaf = 0
            preorder(root, 0)
            return root_to_leaf

        def fxr():
            """
            Runtime: 57 ms, faster than 19.30% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.

            T:O(N)
            """

            def dfs(r: TreeNode, path, res):
                if not r:
                    return
                if not r.left and not r.right:
                    v = 0
                    for n in path + [r.val]:
                        v = v * 2 + int(n)
                    res.append(v)
                    return
                path += [r.val]
                dfs(r.left, path, res)
                dfs(r.right, path, res)
                path.pop()
                return

            res = []
            dfs(root, [], res)
            # print(res)
            return sum(res)
