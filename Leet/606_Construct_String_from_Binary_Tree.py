"""
Tag: Easy, DFS
Lookback:
- careful in logic
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def gongshui3ye():
            """
            https://leetcode-cn.com/problems/construct-string-from-binary-tree/solution/by-ac_oier-i2sk/
            """
            sb = []

            def pre(T: TreeNode):
                nonlocal sb
                sb.append("(")
                if T:
                    sb.append(str(T.val))
                    if T.left:
                        pre(T.left)
                    # if not left subtree but has right subtree, must use () for empty left subtree!
                    elif T.right:
                        sb.append("()")
                    if T.right:
                        pre(T.right)
                sb.append(")")

            pre(root)
            return "".join(sb[1:-1])
