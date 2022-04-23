"""
https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

"""
# Definition for a binary tree node.


from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def fxr():
            """
            Runtime: 24 ms, faster than 98.16% of Python3 online submissions for Binary Tree Right Side View.

            AC in 1.

            """
            # bfs, add last in q to result
            res = []
            if not root:
                return res
            q = deque()
            q.append(root)
            while q:
                qlen = len(q)
                for i in range(qlen):
                    cur = q.popleft()
                    # handle result
                    if i == qlen-1:
                        res.append(cur.val)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)

            return res
        return fxr()
