"""
Tag: Easy, BST
Lookback:
- get clear on the recursion flow, and base case!
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1000/
Leetcode Explore Binary Search Tree
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def iterative():
            cur = root
            while cur:
                if cur.val == val:
                    return cur
                elif cur.val > val:
                    cur = cur.left
                else:
                    cur = cur.right
            return None

        def recur_dbabichev():
            def dfs(T: TreeNode):
                """
                Runtime: 83 ms, faster than 79.14% of Python3 online submissions for Search in a Binary Search Tree.

                XXX: Either if we found place,
                    where these two values are equal,
                    or we reached NULL leaf (it means we visited leaf and descended to its NULL children).
                """
                if not T or T.val == val:
                    return T
                elif T.val > val:
                    return dfs(T.left)
                else:
                    return dfs(T.right)

            return dfs(root)
