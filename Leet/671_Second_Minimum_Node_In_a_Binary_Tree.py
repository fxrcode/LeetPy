"""
✅ GOOD Tree (DFS w/ simple logic)
❌ 
Tag: Easy, DFS
Lookback:
- when stop, when continue dfs?
- it's like Tournament's silver player
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def awice():
            """
            Runtime: 24 ms, faster than 98.47% of Python3 online submissions for Second Minimum Node In a Binary Tree.

            XXX: obvious, min1 is root. if node > min1, it maybe 2nd min, but its subtree >= it, so no need dfs
                when to dfs? Ans: if node.val == min1,
            """
            ans = [float("inf")]
            min1 = root.val

            def dfs(T: TreeNode):
                if T:
                    if min1 < T.val < ans[0]:
                        ans[0] = T.val
                    elif T.val == min1:
                        dfs(T.left)
                        dfs(T.right)

            dfs(root)
            return ans[0] if ans[0] < float("inf") else -1
