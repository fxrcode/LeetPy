"""
✅ GOOD BST (Iterator)
Tag: Medium, BST
Lookback:
- more difficult than #173, due to hasPre
- needs additional var: arr & pointer
[ ] REDO
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    """
    Runtime: 436 ms, faster than 91.85% of Python3 online submissions for Binary Search Tree Iterator II.

    https://leetcode.com/problems/binary-search-tree-iterator-ii/discuss/1948004/Python3-Iterative-Solution-beats-~100
    simpler than OS (no need self.last), while similar to #173
    """

    # T = O(h) where h is height of tree
    def __init__(self, root: Optional[TreeNode]):
        self.stk = []  # for tree traversal
        self.arr = []  # for storing the vals once it's processed
        self.idx = -1  # ptr for self.list
        # initialize stack with first left inorder
        self._left_ino(root)

    def _left_ino(self, T: TreeNode):
        while T:
            self.stk.append(T)
            T = T.left

    def hasNext(self) -> bool:
        return self.stk or self.idx + 1 < len(self.arr)

    # T = O(h)
    def next(self) -> int:
        self.idx += 1
        if self.idx < len(self.arr):
            return self.arr[self.idx]

        topmost = self.stk.pop()
        # update arr in inorder fashion
        self.arr.append(topmost.val)
        # perform left inorder if needed
        self._left_ino(topmost.right)
        return topmost.val

    def hasPrev(self) -> bool:
        return self.idx > 0

    def prev(self) -> int:
        self.idx -= 1
        return self.arr[self.idx]


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()
