"""
tag: dfs, tree
Similar:
572.Subtree-of-Another-Tree
1612. Check If Two Expression Trees are Equivalent
690. Employee Importance

https://leetcode.com/explore/learn/card/recursion-ii/503/recursion-to-iteration/2894/
Leetcode explore Recursion II: Recursion to Iteeration

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

"""

# Definition for a binary tree node.


from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs():
            """
            Runtime: 32 ms, faster than 67.29% of Python3 online submissions for Same Tree.

            """

            def valid(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
                if p and q:
                    return p.val == q.val
                return p == q

            deq = deque([(p, q)])
            while deq:
                cp, cq = deq.popleft()
                if not valid(cp, cq):
                    return False
                if cp:  # XXX: careful! don't miss the check
                    deq.append((cp.left, cq.left))
                    deq.append((cp.right, cq.right))
            return True

        def os_dfs():
            """
            Runtime: 31 ms, faster than 88.30% of Python3 online submissions for Same Tree.

            """

            def dfs(p, q):
                if p and q:
                    return (
                        p.val == q.val and dfs(p.left, q.left) and dfs(p.right, q.right)
                    )
                return p == q

            # if not p and not q:
            #     return True
            # if not p or not q:
            #     return False
            # if p.val != q.val:
            #     return False
            # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
