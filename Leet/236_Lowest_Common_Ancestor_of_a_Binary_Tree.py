'''
https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/932/
Leetcode explore Binary Tree: Conclusion

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Runtime: 555 ms, faster than 5.23% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.

        ??? Why so slow? Both recursive & iterative are O(N) time complexity

        TODO: this is tooo slow, need iterative approach
        StefanPochmann's pythonic code: we extend the meaning of this function:
        * if current (sub)tree contains both p&q, then return lca;
        * if only one of them in the subtree, then return one of them
        * if none in subtree, return None

        XXX: common snippet
        """

        # XXX: cool pythonic: check root for 3 cases
        if root in (None, p, q):
            return root
        # XXX: cool pythonic: return tuple
        l, r = (self.lowestCommonAncestor(kid, p, q)
                for kid in (root.left, root.right))
        return root if l and r else l or r
