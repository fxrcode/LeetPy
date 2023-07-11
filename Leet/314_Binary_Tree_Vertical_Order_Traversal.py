"""
FB tag (Top50)
tag: Medium, BFS

Similar:
- 655.
- 662
"""

from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def os_bfs():
            """
            Runtime: 38 ms, faster than 43.12% of Python3 online submissions for Binary Tree Vertical Order Traversal.

            T: O(N)
            """
            if not root:
                return []

            # (col, node)
            q = deque([(0, root)])
            pos = defaultdict(list)
            mnc, mxc = 0, 0
            while q:
                for _ in range(len(q)):
                    col, nod = q.popleft()
                    mnc, mxc = min(col, mnc), max(col, mxc)
                    pos[col].append(nod.val)
                    if nod.left:
                        q.append((col - 1, nod.left))
                    if nod.right:
                        q.append((col + 1, nod.right))

            ans = []
            for c in range(mnc, mxc + 1):
                ans.append(pos[c])
            return ans

        def fxr():
            """
            Runtime: 66 ms, faster than 7.82% of Python3 online submissions for Binary Tree Vertical Order Traversal.

            T: (CRlogR) # C: #cols, R: #rows
            """
            if root is None:
                return []
            pos = defaultdict(list)
            cols = [0, 0]

            def dfs(r: TreeNode, row, col):
                nonlocal cols
                if r:
                    cols = [min(col, cols[0]), max(col, cols[1])]
                    dfs(r.left, row + 1, col - 1)
                    pos[col].append((row, (r.val)))
                    dfs(r.right, row + 1, col + 1)

            dfs(root, 0, 0)

            res = []
            for c in range(cols[0], cols[1] + 1):
                res.append([v for r, v in sorted(pos[c], key=lambda tu: (tu[0]))])
                # res.append([v for r, v in pos[c]])
            return res
