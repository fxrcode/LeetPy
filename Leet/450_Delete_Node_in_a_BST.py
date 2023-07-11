"""
Daily Challenge (Nov 22)

https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/142/conclusion/1018/
Leetcode Explore Binary Search Tree: Basic Ops

"""
# Definition for a binary tree node.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Runtime: 80 ms, faster than 38.65% of Python3 online submissions for Delete Node in a BST.

        XXX: When you see Binary Tree, instantly think about recursion!
        With recursion, we can hold parent: root, and subtree: deleteNode(root.left/right) so as to link.

        REF: https://leetcode.com/problems/delete-node-in-a-bst/discuss/213685/Clean-Python-3-with-comments-in-details
        """
        if not root:
            return None
        if key > root.val:
            # BUG: return self.deleteNode(root.left, key)
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # BUG: return self.deleteNode(root.left, key)
            root.left = self.deleteNode(root.left, key)
        else:  # key = root.val
            if not root.right:
                # if no right child, just return left child (also works if left=None) to its parent to connect!
                return root.left
            # has right, then 'swap' root/succ, then delete the succ in right sub-tree
            succ = self.successor(root)
            # XXX: Interview Tip: Practice Overriding Your Brains "Assume" Mode! Simply overwrite root.val!
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)
        return root

    def deleteNode_fxr_WA(
        self, root: Optional[TreeNode], key: int
    ) -> Optional[TreeNode]:
        # BUG: https://stackoverflow.com/questions/29809910/reassigning-variables-in-python
        #      you don't understand python var re-assignment.

        # 1st: search for the node
        node = self.query(root, key)
        if not node:
            return root

        # 2nd: 3 cases to delete this node
        #   2.1 no child -> simple del
        #   2.2 1 child -> use the child to overwrite this node
        #   2.3 2 children -> how to maintain BST after delete? use its successor or predeccesor

        # ??? How to del a node???
        # Ans: set this node to none doesn't work! Must set its parent.left/right = None

        if not node.left and not node.right:
            node = None
        elif not node.left or not node.right:
            child = node.left or node.right
            node.val = child.val
            child = None
        else:
            succ = self.successor(node)
            node.val = succ.val
            # del succ
            # succ = None
            # BUG: reassign doesn't change the link of parent, it just make succ another var (None)!!!
            # which means, the node is not deleted.
            # You have to use parent.left/right = Noe to delete!
        return root

    def query(self, root: TreeNode, key: int) -> TreeNode:
        cur = root
        while cur and cur.val != key:
            if cur.val < key:
                cur = cur.right
            else:
                cur = cur.left
        return cur

    def successor(self, root: TreeNode) -> TreeNode:
        root = root.right
        while root.left:
            root = root.left
        return root

    def predessor(self, root: TreeNode) -> TreeNode:
        root = root.left
        while root.right:
            root = root.right
        return root


def debu():
    a = TreeNode(2)
    b = TreeNode(4)
    print(id(b))
    a.right = b
    print(a)
    b = None
    print(a)
    print(id(a.right))
    print(id(b))


root = TreeNode(
    5,
    left=TreeNode(3, left=TreeNode(2), right=TreeNode(4)),
    right=TreeNode(6, right=TreeNode(7)),
)

sl = Solution()
# sl.deleteNode_fxr_WA(root, 3)

debu()
