'''
https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/943/
Leetcode explore Binary Tree: Conclusion

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
'''

# Definition for a binary tree node.


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Your runtime beats 79.16 % of python3 submissions.
        XXX: same logic as 106, but be careful on index!
            eg. follow specific examples to calculate the index
        AC in 1st try, but I did run test to find my index bug
        """
        self.inV2I = {v: i for i, v in enumerate(inorder)}

        def bottom_up(pl, pr, il, ir):
            # base
            if pl > pr or il > ir:
                return None

            rootV = preorder[pl]
            root = TreeNode(rootV)
            iroot_idx = self.inV2I[rootV]
            nums_left = iroot_idx - il
            root.left = bottom_up(pl+1, pl+nums_left, il, iroot_idx-1)
            root.right = bottom_up(pl+nums_left+1, pr, iroot_idx+1, ir)
            return root
            # recur

        return bottom_up(0, len(preorder)-1, 0, len(inorder)-1)
