"""
tag: Medium, BST, FB, inorder
Lookback: 
always trust your recursion that will do its job, so focus on local view!
same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/
[ ] TODO: iterative
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def mandavawala_fxr():
            """
            Runtime: 66 ms, faster than 5.02% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.

            XXX: small change from mandavawala, simply update param: acc along the way, so no need of return
            T: O(N)
            """

            def ino(r: TreeNode, acc):
                if r:
                    ino(r.right, acc)
                    r.val += acc[0]
                    acc[0] = r.val
                    ino(r.left, acc)
                    return r

            ino(root, [0])
            return root

        def lee215():
            """
            Runtime: 60 ms, faster than 6.69% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.

            T: O(N)
            """
            pre = 0

            def inord(r: TreeNode):
                nonlocal pre
                if r:
                    inord(r.right)
                    r.val = pre = pre + r.val
                    inord(r.left)
                    return r

            return inord(root)

        def mandavawala():
            """
            Runtime: 48 ms, faster than 23.95% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.

            """

            def ino(r: TreeNode, sumTillNow):
                if not r:
                    return sumTillNow
                sr = ino(r.right, sumTillNow)
                r.val += sr
                return ino(r.left, r.val)

            ino(root, 0)
            return root
