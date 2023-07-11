"""
Mock by Chris (FB phone) Dec 22, 2021

Metacognition: I was hesitate on calculate complete subtree directly, cuz I didn't think through the simple logic
    to see if the subtree is complete... Also, I got bug on counting lh, so I init it to 1, which leads to extra +1.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 64 ms, faster than 98.50% of Python3 online submissions for Count Complete Tree Nodes.

        AC after Chris give me hint on direct calc if current subtreee is complete
        """

        def dfs(node):
            if not node:
                return 0
            # BUG: lh=rh=1 (because while l only exit when l is None, so lh will +1 when l=None, and exit in next round)
            lh = rh = 0
            l = r = node
            while l:
                l = l.left
                lh += 1
            while r:
                r = r.right
                rh += 1
            if lh == rh:
                print(node.val, lh)
                return 2**lh - 1
            else:
                return 1 + dfs(node.left) + dfs(node.right)

        return dfs(root)
