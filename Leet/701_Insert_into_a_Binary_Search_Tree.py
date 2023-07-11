"""
✅ GOOD DFS (post-order)

https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1003/
Leetcode Explore Binary Search Tree: Basic Ops
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST_recur(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        """
        Runtime: 189 ms, faster than 21.22% of Python3 online submissions for Insert into a Binary Search Tree.

        https://leetcode.com/problems/insert-into-a-binary-search-tree/solution/

        T: O(h)
        XXX: think about recursion I learned from CS 106B 2015, but the base case might not be in 1st line!
            flexibly use template, rather owned by (or stuck in) template!
        """

        def dfs(node: TreeNode) -> TreeNode:
            if not node:
                return TreeNode(val)
            if node.val < val:
                node.right = dfs(node.right)
            else:
                node.left = dfs(node.left)
            return node

        return dfs(root)

    '''
    def insertIntoBST_fxr(self, root: Optional[TreeNode],
                          val: int) -> Optional[TreeNode]:
        """
        Runtime: 128 ms, faster than 94.66% of Python3 online submissions for Insert into a Binary Search Tree.
        XXX: This is bad DFS style! You should learn post-order dfs, rather dfs without return!
        """
        def dfs(node, v):
            if v < node.val:
                if node.left:
                    dfs(node.left, val)
                else:
                    node.left = TreeNode(val)
                    return
            else:
                if node.right:
                    dfs(node.right, val)
                else:
                    node.right = TreeNode(val)
                    return

        if not root:
            return TreeNode(val)
        dfs(root, val)
        return root
    '''

    def insertIntoBST_iter(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root:
            return node
        pre, cur = None, root
        while cur:
            pre = cur
            if val > cur.val:
                # go right
                cur = cur.right
            else:
                # go left
                cur = cur.left
        # now pre is the leaf which should be node's parent, how to decide which child? easy!
        if val < pre.val:
            pre.left = node
        else:
            pre.right = node
        return root

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Your runtime beats 69.54 % of python3 submissions.

        AC in 1
        The 200-th question solved in Leetcode @ Oct 10, 2021
        """
        cur = root
        pre = None
        dir = 0
        node = TreeNode(val)
        if not root:
            return node
        while cur:
            pre = cur
            if cur.val < val:
                cur = cur.right
                dir = 1
            else:
                cur = cur.left
                dir = 0
        # now right pos

        if dir:
            pre.right = node
        else:
            pre.left = node
        return node
