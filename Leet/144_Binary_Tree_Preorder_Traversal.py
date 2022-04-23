'''
手把手刷二叉树系列完结篇

'''

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def labuladong_iter():
            """
            Runtime: 49 ms, faster than 21.38% of Python3 online submissions for Binary Tree Preorder Traversal.

            REF: https://labuladong.github.io/algo/2/18/33/
            """
            stk, visited = [], TreeNode(None)
            ret = []

            def pushleftbranch(r: TreeNode):
                while r:
                    # preorder
                    ret.append(r.val)
                    stk.append(r)
                    r = r.left

            pushleftbranch(root)
            while stk:
                p = stk[-1]
                # p.left subtree done, but p.right not
                if (not p.left or p.left == visited) and p.right != visited:
                    # inorder
                    pushleftbranch(p.right)
                # p.right subtree done
                if not p.right or p.right == visited:
                    # postorder
                    visited = stk.pop()

            return ret

        return labuladong_iter()

        def labuladong_backtrack():
            res = []

            def traverse(node):
                if not node:
                    return
                nonlocal res
                res.append(node.val)
                traverse(node.left)
                traverse(node.right)

            traverse(root)
            return res

        def labuladong_dp():
            def dp(node):
                res = []
                if not node:
                    return res
                res.append(node.val)
                res.extend(dp(node.left))
                res.extend(dp(node.right))
                # XXX: Don't forget if dfs has return val!!!
                return res

            return dp(root)


root = TreeNode(1,
                left=TreeNode(2,
                              left=TreeNode(5),
                              right=TreeNode(4,
                                             left=TreeNode(6),
                                             right=TreeNode(7))),
                right=TreeNode(3, left=TreeNode(8), right=TreeNode(9)))
# root = TreeNode(1,
#                 left=TreeNode(2),
#                 right=TreeNode(3,
#                                left=TreeNode(8),
#                                right=TreeNode(9))
#                 )

sl = Solution()
print(sl.preorderTraversal(root))
