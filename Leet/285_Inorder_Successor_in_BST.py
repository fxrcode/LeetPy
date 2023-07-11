"""
✅ GOOD DFS (Inorder)

https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/140/introduction-to-a-bst/998/
Leetcode Explore Binary Search Tree: Conclusion
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor_recur(self, root: "TreeNode", p: "TreeNode") -> "TreeNode":
        """
        https://leetcode.com/problems/inorder-successor-in-bst/discuss/72653/Share-my-Java-recursive-solution

        XXX: Code walkthrough for Successor:
        First we go to exact path of node till end which we want to find out using BST property.
        Use back track, Consideration for every node while back track
        (a). For every node if we backtrack from right side then simply return because successor will be its parent.
        (b). If we backtrack from left side, then successor will be Either current node OR any successor found in left subtree.
        """

        def succesor(root: "TreeNode"):
            if not root:
                return None
            if root.val <= p.val:
                return succesor(root.right)
            else:
                left = succesor(root.left)
                return left if left else root

        def predessor(root: TreeNode):
            if not root:
                return None
            if root.val > p.val:
                return predessor(root.left)
            else:
                right = predessor(root.right)
                return right if right else root

    def inorderSuccessor_sol(self, root: "TreeNode", p: "TreeNode") -> "TreeNode":
        """
        Your runtime beats 95.14 % of python3 submissions.

        T: O(logN)
        """

        def succ_itere(root: TreeNode):
            succ = None
            while root:
                if p.val >= root.val:
                    root = root.right
                else:
                    succ = root
                    root = root.left
            return succ

        def pred_iter(root: TreeNode):
            pred = None
            while root:
                if p.val > root.val:
                    pred = root
                    root = root.right
                else:
                    root = root.left
            return pred

    def inorderSuccessor_sol_I(self, root: "TreeNode", p: "TreeNode") -> "TreeNode":
        """
        Your runtime beats 72.46 % of python3 submissions.

        T: O(N)

        XXX: Classical Tree interview question.
        * inorder successor for general binary tree. Because interviewer may first ask this :)
        * solved by 2 different cases
        """

        def case2(cur):
            # generic base case for traversal
            if not cur:
                return
            case2(cur.left)

            # XXX: essense: first time really use inorder traversal, rather simple print.
            if self.previous == p and not self.inorder_succ:
                self.inorder_succ = cur
                return
            self.previous = cur

            case2(cur.right)

        self.previous, self.inorder_succ = None, None
        # case 1
        if p.right:
            leftmost = p.right
            while leftmost.left:
                leftmost = leftmost.left
            self.inorder_succ = leftmost
        else:  # case 2
            case2(root)
        return self.inorder_succ
