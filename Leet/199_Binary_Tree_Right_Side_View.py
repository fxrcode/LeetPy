"""
Tag: Medium, DFS, BFS
Lookback:
- Top 100 Liked Questions
- 1/3 of 545: Boundary of Binary Tree
"""
# Definition for a binary tree node.


from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs_545():
            res = []
            if not root:
                return res

            def dfs(T: TreeNode):
                if not T:
                    return
                if T.right:
                    dfs(T.right)
                else:
                    dfs(T.left)
                res.append(T.val)

            dfs(root)

            return res[::-1]

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
                    if i == qlen - 1:
                        res.append(cur.val)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)

            return res

        return fxr()
