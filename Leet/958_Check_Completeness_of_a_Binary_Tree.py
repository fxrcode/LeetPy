"""
✅ GOOD Tree (BFS vs DFS)
Tag: Medium, BFS, DFS
Lookback:
- practice to re-state for every problem!
- completeness === there shouldn't be any node 
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def lee215_dfs():
            """
            https://leetcode.com/problems/check-completeness-of-a-binary-tree/discuss/205682/JavaC%2B%2BPython-BFS-Solution-and-DFS-Soluiton
            property of FULL tree: #nodes = 2^k-1. bit hack: x = 2^k-1, then x&(x+1) = 0
            """

            def dfs(T: TreeNode):
                if not T:
                    return 0
                l, r = dfs(T.left), dfs(T.right)
                if l & (l + 1) == 0 and l // 2 <= r <= l:
                    return l + r + 1
                if r & (r + 1) == 0 and r <= l <= r * 2 + 1:
                    return l + r + 1
                return -1

            return dfs(root) > 0

        def brianchiang_bfs():
            """
            Runtime: 23 ms, faster than 99.94% of Python3 online submissions for Check Completeness of a Binary Tree.
            https://leetcode.com/problems/check-completeness-of-a-binary-tree/discuss/533798/Python-O(n)-by-level-order-traversal.-90%2B-w-Diagram
            """
            q = deque([root])
            pre = root
            while q:
                # have_none = False # WA: [1,2,3,4,5,6,7,8,9,10,11,12,13,null,null,15]
                for _ in range(len(q)):
                    cur = q.popleft()
                    if cur:
                        if not pre:
                            return False
                        q.append(cur.left)
                        q.append(cur.right)
                    pre = cur
            return True

        """
        def fxr_WA():
            # failed: [1,2,3,4,5]
            q = deque([root])
            while q:
                n = len(q)
                cnt = 0
                for i in range(n):
                    cur = q.popleft()
                    if i == n - 1:
                        if cnt != (n - 1) * 2:
                            return False
                        if not cur.left and cur.right:
                            return False
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            return True
        """
