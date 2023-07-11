"""
Weekly Special (Jan W4)
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        def os_dfs():
            """
            Runtime: 461 ms, faster than 46.87% of Python3 online submissions for Find Nearest Right Node in Binary Tree.

            T: O(N)
            """
            if not root:
                return None
            q = deque([root])
            while q:
                qlen = len(q)
                for i in range(qlen):
                    cur = q.popleft()
                    if cur == u:
                        return q.popleft() if i != qlen - 1 else None
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)

        def fxr_bfs():
            """
            Runtime: 432 ms, faster than 34.61% of Python3 online submissions for Find Nearest Right Node in Binary Tree.

            T: O(N)
            """
            q = deque([root])
            while q:
                qlen = len(q)
                for i in range(qlen):
                    cur = q.popleft()
                    if cur == u:
                        if i == qlen - 1:
                            return None
                        else:
                            return q[0]
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            return None
