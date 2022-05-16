"""
Tag: Medium, BFS, DFS
Lookback:
- DFS is always more elegant
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dbabichev_dfs():
            """
            Runtime: 358 ms, faster than 24.33% of Python3 online submissions for Deepest Leaves Sum.

            https://leetcode.com/problems/deepest-leaves-sum/discuss/1153045/Python-2-dfs-explained
            T: O(N), M: O(h)
            """

            def dep(T: TreeNode):
                if not T:
                    return 0
                return max(dep(T.left), dep(T.right)) + 1

            def dfs(T: TreeNode, d: int) -> int:
                if not T:
                    return 0
                if d == 0:
                    return T.val
                else:
                    return dfs(T.left, d - 1) + dfs(T.right, d - 1)

            return dfs(root, dep(root) - 1)

        def fxr():
            """
            Runtime: 208 ms, faster than 94.19% of Python3 online submissions for Deepest Leaves Sum.

            XXX: forgot BFS template after 1 week gap... SUCKS
            """
            bfs = deque([root])
            ans = 0
            while bfs:
                ans = 0
                for _ in range(len(bfs)):
                    n = bfs.popleft()
                    ans += n.val
                    for k in [n.left, n.right]:
                        if k:
                            bfs.append(k)
            return ans

        return fxr()
