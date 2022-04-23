"""
💡insight Logic 
✅ GOOD BST
Daily Challenge (Dec 14)
tag: medium, BST, dfs, logic
Lookback:
- BST => prune or in-order

[ ] REDO
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dbabichev():
            """
            Runtime: 216 ms, faster than 90.80% of Python3 online submissions for Range Sum of BST.

            https://leetcode.com/problems/range-sum-of-bst/discuss/936480/Python-Simple-dfs-explained

            1) Check value node.val and if it is in our range, add it to global sum.
            2) We need to visit left subtree only if node.val > low, that is if node.val < low,
                it means, that all nodes in left subtree less than node.val, that is less than low as well.
            3) Similarly, we visit right subtree only if node.val < high.

            T: O(m). # m = number of nodes in [low,high]
            """

            def dfs(node: TreeNode):
                if not node:
                    return
                nonlocal ans
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)

            ans = 0
            dfs(root)
            return ans
