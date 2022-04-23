'''
tag: easy, DFS, BST
Lookback:
- similar to 847. shortest path visiting all nodes?
- BST dfs trick: low/hi bound.
'''

from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def leetcoder289():
            """
            Runtime: 75 ms, faster than 57.45% of Python3 online submissions for Minimum Absolute Difference in BST.

            https://leetcode.com/problems/minimum-absolute-difference-in-bst/discuss/338515/Python-recursive
            T: O(N), M: O(h)
            """

            def f(node: TreeNode, lo, hi):
                if not node:
                    return hi - lo
                l = f(node.left, lo, node.val)
                r = f(node.right, node.val, hi)
                return min(l, r)

            return f(root, -2e9, 2e9)

        def awise():
            """
            Runtime: 52 ms, faster than 96.14% of Python3 online submissions for Minimum Absolute Difference in BST.
            https://leetcode.com/problems/minimum-absolute-difference-in-bst/discuss/99910/Python-Simple-(Inorder-Traversal)
            https://realpython.com/python-is-identity-vs-equality/#comparing-the-python-comparison-operators

            T: O(N), M: O(h)
            """
            mn = 2e9
            pre = None

            def ino(r: TreeNode):
                if r.left:
                    ino(r.left)
                nonlocal pre, mn
                '''
                WA: 187 / 188 test cases passed. [0,null,2236,1277,2776,519]. Expected: 519. Output: 540.
                BUG: fail for pre == 0!
                if pre: 
                '''
                if pre is not None:
                    mn = min(mn, r.val - pre)
                pre = r.val
                if r.right:
                    ino(r.right)

            ino(root)
            return mn