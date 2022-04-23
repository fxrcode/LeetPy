"""
dfs tag (Medium)
[ ] REDO
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        '''
        def dfs(node, target):
            """
            Runtime: 88 ms, faster than 5.18% of Python3 online submissions for Path Sum II.
            OS impl
            T: O(N^2)
            """
            if not node:
                return []
            if not node.left and not node.right:
                if target == node.val:
                    return [[node.val]]
                else:
                    return []
            subs = dfs(node.left, target - node.val) + \
                dfs(node.right, target - node.val)
            return [[node.val] + sub for sub in subs]

        return dfs(root, targetSum)
        '''

        def fxr_dfs(node, target, path, res):
            """
            Runtime: 75 ms, faster than 14.32% of Python3 online submissions for Path Sum II.

            XXX: still recursion! rather divide-conquer DFS (use sub's return)
            T: O(N)
            """
            if not node:
                return
            if not node.left and not node.right:
                if node.val == target:
                    res.append(path + [node.val])
                    return
            target -= node.val
            fxr_dfs(node.left, target, path + [node.val], res)
            fxr_dfs(node.right, target, path + [node.val], res)

        res = []
        fxr_dfs(root, targetSum, [], res)
        return res


sl = Solution()
root = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
targetSum = 3

print(sl.pathSum(root, targetSum))
