'''
https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/1016/
Leetcode explore Binary Tree: Conclusion
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
XXX: Good question to understand variation top-down (aka preorder with recursion right before recursion left) recursion
XXX: Draw the nice cases given in forum (leetcode, leetcode-cn to better understand why rec(right) before rec(left))
'''
# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        Your runtime beats 55.96 % of python3 submissions.

        Consider this: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/172861/Mostly-recursive-solution-O(n)-time-(beats-99.32)-and-O(1)-space-(without-considering-stack)/219440
        XXX: Crux: rec(right) before rec(left): https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/comments/45416
        if recursively call left first, 7 can not find next node to connect due to the gap of 5->6.
             1    ->  2
            /  \     / \
           3 -> 4 ->5   6
          /              \
         7                 8
        """

        def fnext(root: Node) -> Node:
            if not root:
                return root
            if root.left or root.right:
                return root.left or root.right
            return fnext(root.next)

        def topdown(root: Node) -> Node:
            # process root
            if not root:
                return root
            if root.left:
                if root.right:
                    root.left.next = root.right
                else:
                    root.left.next = fnext(root.next)
            if root.right:
                root.right.next = fnext(root.next)

            # XXX: process right before left to prepare the next!!!
            topdown(root.right)
            topdown(root.left)
            return root

        return topdown(root)

    def connect_BFS(self, root: Node) -> Node:
        """
        Runtime: 48 ms, faster than 78.31% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
        """
        if not root:
            return root
        q = deque([root])
        while q:
            qlen = len(q)
            pre = None
            for _ in range(qlen):
                cur = q.popleft()
                if pre:
                    pre.next = cur
                pre = cur
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root
    '''
    def connect(self, root: 'Node') -> 'Node':
        """
        WA: [1,2,3,4,5,null,6,7,null,null,null,null,8]
        """
        if not root or (not root.left and not root.right):
            return root
        if root.left:
            root.left.next = root.right
        if root.next:
            if root.right:
                root.right.next = root.next.left or root.next.right
            else:
                root.left.next = root.next.left or root.next.right
        self.connect(root.left)
        self.connect(root.right)
        return root
    '''
