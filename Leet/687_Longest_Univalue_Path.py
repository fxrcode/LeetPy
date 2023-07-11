"""
✅ GOOD DFS (post-order)
tag: Medium, DFS
Lookback:
- classic post-order dfs
- disguise of 543/1522. Diameter of Tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def diameter_yangshun():
            """
            Runtime: 353 ms, faster than 96.33% of Python3 online submissions for Longest Univalue Path.

            disguise of 543/1522. Diameter of Tree
            https://leetcode.com/problems/longest-univalue-path/discuss/108142/Python-Simple-to-Understand/110423
            """
            longest = 0

            def dfs(node: TreeNode, fa):
                # longest uni-value branch's #edges from node to leaf
                if not node:
                    return 0
                left, right = dfs(node.left, node.val), dfs(node.right, node.val)
                nonlocal longest
                longest = max(longest, left + right)
                return 1 + max(left, right) if node.val == fa else 0

            dfs(root, None)
            return longest

        def fxr():
            """
            Runtime: 352 ms, faster than 96.71% of Python3 online submissions for Longest Univalue Path.

            """
            mx = 0

            def post(node: TreeNode):
                if not node:
                    return 0
                pass_node = 0
                longest = 1
                nonlocal mx
                for kid in (node.left, node.right):
                    branch = post(kid)
                    # print(kid, side)
                    if kid and kid.val == node.val:
                        pass_node += branch
                        longest = max(longest, 1 + branch)
                mx = max(mx, pass_node)
                return longest

            post(root)
            return mx

        return fxr()


root = TreeNode(
    5,
    left=TreeNode(5, left=TreeNode(5), right=TreeNode(5)),
    right=TreeNode(5, right=TreeNode(5)),
)
sl = Solution()
print(sl.longestUnivaluePath(root))
