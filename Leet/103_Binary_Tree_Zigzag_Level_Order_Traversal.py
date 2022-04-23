"""
Top Amazon
tag: medium
Lookback
- trick to alter list vs reverse list: [::direction], where direction = (+/-)1.
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def os_dfs():
            """
            Runtime: 51 ms, faster than 40.34% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.

            Though not intuitive, we could also obtain the BFS traversal ordering via the DFS (Depth-First Search) traversal in the tree.
            T: O(N), M: O(H)
            """
            if not root:
                return []

            res = []

            def dfs(r: TreeNode, level: int):
                if level >= len(res):
                    res.append(deque([r.val]))
                else:
                    if level % 2 == 0:
                        res[level].append(r.val)
                    else:
                        res[level].appendleft(r.val)

                for kid in [r.left, r.right]:
                    if kid:
                        dfs(kid, level + 1)

            dfs(root, 0)
            return res

        def dbabichev():
            if not root:
                return []
            q = deque([root])
            res, direction = [], 1
            while q:
                level = []
                for _ in range(len(q)):
                    n = q.popleft()
                    level.append(n.val)
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                res.append(level[::direction])  #!trick
                direction *= -1
            return res

        def fxr_bfs():
            """
            Runtime: 30 ms, faster than 92.49% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.

            """
            res = []
            q = [root]
            even = True
            while q:
                nxt = []
                res.append([])
                for n in q:
                    res[-1].append(n.val)
                    for kid in (n.left, n.right):
                        if kid:
                            nxt.append(kid)
                if not even:
                    res[-1].reverse()
                even = not even
                q = nxt
            return res
