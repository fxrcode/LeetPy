'''
https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/942/
Leetcode explore Binary Tree: Conclusion

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.


Metacognition:
* 2nd do: I found [lo,hi] is better to be both inclusive is easier! Let me stick with it.
        And OS solution only needs inorder lo,hi pointer, but have to dfs(right part), then dfs(left part), since its always postorder.pop()
'''

# Definition for a binary tree node.


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Your runtime beats 86.80 % of python3 submissions.
        AC in 1.
        XXX: postorder: left-post, right-post, root
             inorder: left-in, root, right-in
        """
        self.inV2I = {v: i for i, v in enumerate(inorder)}

        def dfs(il, ir, pl, pr):
            # base
            if ir < il or pr < pl:
                return None

            rootv = postorder[pr]
            root = TreeNode(rootv)
            iroot_idx = self.inV2I[rootv]
            nums_left = iroot_idx - il
            # recurrent
            root.left = dfs(il, iroot_idx-1, pl, pl+nums_left-1)
            root.right = dfs(iroot_idx+1, ir, pl+nums_left, pr-1)
            return root

        return dfs(0, len(inorder)-1, 0, len(postorder)-1)
