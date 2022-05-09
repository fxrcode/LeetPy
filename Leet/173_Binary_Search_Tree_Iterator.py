"""
✅ GOOD BST (Iterator)
Tag: Medium, BST
Lookback:
- careful in logic detail
- maintain invariant in next()
Similar:
1586: w/ pre & next
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/140/introduction-to-a-bst/1008/
Leetcode Explore Binary Search Tree

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class BSTIterator:
    """
    Runtime: 78 ms, faster than 80.47% of Python3 online submissions for Binary Search Tree Iterator.

    """

    def __init__(self, root: Optional[TreeNode]):
        self.stk = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, T: TreeNode):
        while T:
            self.stk.append(T)
            T = T.left

    def next(self) -> int:
        # Invariant: Node at the top of the stack is the next smallest element
        topmost = self.stk.pop()
        # Need to maintain the invariant. If the node has a right child, call the helper function for the right child
        if topmost.right:
            self._leftmost_inorder(topmost.right)
        return topmost.val

    def hasNext(self) -> bool:
        return len(self.stk) > 0


class BSTIterator_pochmann:
    """
    https://leetcode.com/problems/binary-search-tree-iterator/discuss/52647/Nice-Comparison-(and-short-Solution)
    StefanPochmann: How to think about iterator? Ans: write normal traversal with stack, then find the similar pattern
    """

    def __init__(self, root: Optional[TreeNode]):
        self.visit = root
        self.stk = []

    def next(self) -> int:
        # BUG: while self.hasNext():
        while self.visit:
            self.stk.append(self.visit)
            self.visit = self.visit.left
        next = self.stk.pop()
        self.visit = next.right
        return next.val

    def hasNext(self) -> bool:
        return self.visit or self.stk


# Your BSTIterator object will be instantiated and called as such:


root = TreeNode(7, left=TreeNode(3), right=TreeNode(15, left=TreeNode(9), right=TreeNode(20)))
obj = BSTIterator(root)
n1 = obj.next()
hn1 = obj.hasNext()
print(n1, hn1)
