"""
✅ GOOD inorder DFS

https://leetcode.com/explore/learn/card/recursion-ii/507/beyond-recursion/2899/
Leetcode explore Recursion II: Conclusion

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

Similar Inorder Recursion: 285. Inorder Successor in BST.
XXX: Official solution's GIF is so gooooooooooooooood!

"""

# Definition for a Node.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: "Node") -> "Node":
        """
        Runtime: 36 ms, faster than 73.66% of Python3 online submissions for Convert Binary Search Tree to Sorted Doubly Linked List.
        T: O(N), M: O(H)
        """
        self.first = self.last = None

        def inord(cur: Node):
            if not cur:
                return
            inord(cur.left)
            if self.last:
                self.last.right = cur
                cur.left = self.last
            if not self.first:
                # only trigger once: leftmost
                self.first = cur
            self.last = cur
            inord(cur.right)

        inord(root)
        self.first.right = self.last
        self.last.left = self.first
        return self.first
