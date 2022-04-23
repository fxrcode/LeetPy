"""
💡insight (Tree=>Graph)
✅ GOOD DFS/BFS
tag: medium, DFS, BFS,tree, graph, FB
Lookback:
- build parents mapping rather full graph AL, b/c we just need fa for neighbors in search (BFS/DFS)
- dist K from target can use BFS, but DFS works as always (just need to prevent return back to trace, so use prev)
[ ] REDO
"""

from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def os_percolate_dist():
            """
            Approach 2: Percolate Distance

            """
            pass

        def cn_englishyang_dfs():
            """
            https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/solution/er-cha-shu-zhong-suo-you-ju-chi-wei-kde-nlct0/
            Runtime: 37 ms, faster than 89.31% of Python3 online submissions for All Nodes Distance K in Binary Tree.
            Memory Usage: 14.2 MB, less than 98.24% of Python3 online submissions for All Nodes Distance K in Binary Tree.
            """
            fas = {}

            def find_fa(node, fa=None):
                if node:
                    fas[node] = fa
                    find_fa(node.left, node)
                    find_fa(node.right, node)

            res = []

            def walk(node, prev, k):
                if not node:
                    return
                if k == 0:
                    res.append(node.val)
                    return
                for v in (node.left, node.right, fas.get(node)):
                    if v != prev:
                        walk(v, node, k - 1)

            find_fa(root)
            walk(target, None, k)
            return res

        def graph_dfs_bfs():
            """
            Runtime: 32 ms, faster than 98.61% of Python3 online submissions for All Nodes Distance K in Binary Tree.

            XXX: lee215: reduce problem to graph, then simple to solve?
            https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/solution/208166
            """
            u2fa = {}

            def dfs(node: TreeNode, fa=None):
                if node:
                    u2fa[node] = fa
                    dfs(node.left)
                    dfs(node.right)

            dfs(root, None)

            q = deque([(target, 0)])
            seen = {target}
            while q:
                u, d = q.popleft()
                if d == k:
                    return [u.val] + [n.val for n, d in q]
                for v in (u.left, u.right, u2fa[u]):
                    if v and v not in seen:
                        seen.add(v)
                        q.append((v, d + 1))
            return []
