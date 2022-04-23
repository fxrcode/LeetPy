"""
tag: Medium, DFS, BFS
Lookback:
- [ ] REDO
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        def wangqiuc_dfs():
            """
            Runtime: 125 ms, faster than 77.44% of Python3 online submissions for Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree.

            """

            def dfs(i, node: TreeNode):
                if not node or i == n or arr[i] != node.val:
                    return False
                if i == n - 1 and not (node.left or node.right):
                    return True
                return dfs(i + 1, node.left) or dfs(i + 1, node.right)

            n = len(arr)
            return dfs(0, root)
