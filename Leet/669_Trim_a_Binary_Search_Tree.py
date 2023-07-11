"""
❌ REDO
Tag: Medium, DFS
Lookback:
- re-link rather remove
- simply compare w/ low/high, no need of refined range.

https://leetcode.com/list?selectedList=5f4y8dwj
Must Do Easy Questions

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
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        def DBabichev():
            """
            Runtime: 48 ms, faster than 83.75% of Python3 online submissions for Trim a Binary Search Tree.

            XXX: This problem becomes easy when you understand the logic behind trimming.
            """

            def dfs(T: TreeNode) -> TreeNode:
                if not T:
                    return T
                if T.val > high:
                    return dfs(T.left)
                elif T.val < low:
                    return dfs(T.right)
                else:
                    T.left = dfs(T.left)
                    T.right = dfs(T.right)
                    return T

            return dfs(root)

        def fxr():
            """
            Runtime: 52 ms, faster than 66.05% of Python3 online submissions for Trim a Binary Search Tree.

            AC in 1 after 30 min debugging...
            """

            def dfs(node: TreeNode, parent: TreeNode):
                print("\tdfs", node)
                if not node:
                    return None
                nl = dfs(node.left, node)
                nr = dfs(node.right, node)
                if node.val in range(low, high + 1):
                    print(node, "in")
                    node.left = nl
                    node.right = nr
                    return node
                elif node.val < low:
                    print(node, "<")
                    if node == parent.left:
                        parent.left = nr
                    else:
                        parent.right = nr
                    return nr
                else:
                    print(node, ">")
                    if node == parent.left:
                        parent.left = nl
                    else:
                        parent.right = nl
                    return nl

            INF = 1e6
            dummy = TreeNode(INF, left=root)
            ret = dfs(root, dummy)
            return dummy.left

        # return fxr()
        return trim(root)


# root = TreeNode(1, left=TreeNode(0), right=TreeNode(2))
# root = TreeNode(1, right=TreeNode(2))
root = TreeNode(
    3, left=TreeNode(0, right=TreeNode(2, left=TreeNode(1))), right=TreeNode(4)
)
sl = Solution()
sl.trimBST(root, 1, 3)
