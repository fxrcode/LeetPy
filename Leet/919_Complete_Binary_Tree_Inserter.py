'''
✅ GOOD BFS
FB tag (medium)

Complete Tree
[ ] REDO
'''

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    """
    Runtime: 95 ms, faster than 33.90% of Python3 online submissions for Complete Binary Tree Inserter.

    T: O(N)
    """
    def __init__(self, root):
        self.ps = deque()
        self.root = root
        q = deque([root])
        while q:
            c = q.popleft()
            if not c.left or not c.right:
                self.ps.append(c)
            if c.left:
                q.append(c.left)
            if c.right:
                q.append(c.right)

    def insert(self, v):
        p = self.ps[0]
        self.ps.append(TreeNode(v))
        if not p.left:
            p.left = self.ps[-1]
        else:
            p.right = self.ps[-1]
            self.ps.popleft()
        return p.val

    def get_root(self):
        return self.root